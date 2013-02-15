import threading
import util
from abc import abstractmethod
import pickle


class _ReferenceBase(object):
    '''
    Whenever we have a reference, ie a variable, map, list, struct, it
    derives from this.
    '''
    # FIXME: maybe create a separate commit lock instead of
    # re-purposing the no one else can use the commit lock until....

    
    def __init__(self,peered,init_val,version_obj,dirty_element_constructor):
        self.uuid = util.generate_uuid()
        self.version_obj = version_obj
        self.peered = peered
        
        self.val = init_val
        self.dirty_element_constructor = dirty_element_constructor
        
        # keys are uuids.  values are dirty values of each object.
        self._dirty_map = {}
        self._mutex = threading.Lock()

    def _lock(self):
        self._mutex.acquire()
    def _unlock(self):
        self._mutex.release()

    @staticmethod
    def var_type():
        '''
        @returns {String} --- Each subtype of _ReferenceBase has a
        unique name.
        '''
        util.logger_assert(
            'var_type is pure virtual in _ReferenceBase.')

    @abstractmethod
    def copy(self,invalid_listener,peered):
        '''
        Returns a deep copy of this object.  
        '''
        util.logger_assert(
            'copy is pure virtual in _ReferenceBase.')

    @abstractmethod
    def is_value_type(self):
        '''
        @returns {bool} --- True if the reference base points at a
        value type (Text, Bool, Number).  False otherwise.
        '''
        util.logger_assert(
            'is_value_type is pure virtual in _ReferenceBase.')
        
        
    def serializable_var_map_for_network(
        self,var_name,invalid_listener):
        '''
        The runtime automatically synchronizes data between both
        endpoints.  When one side has updated a peered variable, the
        other side needs to attempt to apply those changes before
        doing further work.  This method grabs the val and version
        object of the dirty element associated with invalid_listener.
        Using these data, plus var_name, it constructs a named tuple
        for serialization.  (@see
        util._generate_serialization_named_tuple)

        Note: if the val of this object is another Reference object,
        then we recursively keep generating named tuples and embed
        them in the one we return.

        Note: we only serialize peered data.  No other data gets sent
        over the network; therefore, it should not be serialized.

        @param {String} var_name --- Both sides of the connection need
        to agree on a common name for the variable being serialized.
        This is to ensure that when the data are received by the other
        side we know which variable to put them into.  This value is
        only really necessary for the outermost wrapping of the named
        type tuple, but we pass it through anyways.

        '''

        # FIXME: eventually want to do serialize deltas of variables
        # and version objects instead of full things.
        
        #### DEBUG
        if not self.peered:
            util.logger_assert(
                'Should not be serializing a non-peered data item.')
        #### END DEBUG

            
        self._lock()
        self._add_invalid_listener(invalid_listener)
        dirty_element = self._dirty_map[invalid_listener.uuid]
        self._unlock()


        # a val can either point to a waldo reference, a python value,
        # or a list/map of waldo references or a list/map of python
        # values.
        var_data = dirty_element.val
        if isinstance(var_data,_ReferenceBase):
            var_data = dirty_element.val.serializable_var_map_for_network(
                var_name,invalid_listener)
        elif isinstance(var_data,list) or isinstance(var_data,dict):
            keys = range(0,len(var_data))
            if isinstance(var_data,dict):
                keys = var_data.keys()
            
            for index in keys:
                if isinstance(var_data,_ReferenceBase):
                    var_data[index] = var_data[index].serializable_var_map_for_network(
                        var_name,invalid_listener)

        version_obj_data = dirty_element.version_obj.serializable_for_network_data()

        to_return = util._generate_serialization_named_tuple(
            var_name,self.var_type(),var_data,version_obj_data)
        return to_return

    
    
    def _non_waldo_copy(self):
        '''
        When we are establishing dirty map elements, we make a copy of
        our committed value so that changes do not polute the
        committed val.  (For instance, if val is a python list, we do
        not want an invalidation listener's deletion of elements to be
        visible until the invalidation listener has been committed.)

        However, if val holds an object derived from _ReferenceBase,
        then we just want to return that object itself (because we
        know that it can handle delaying exposing side effects until
        commit).

        self.val can only contain value types or lists of
        values/_ReferenceBases or dicts of values/_ReferenceBases.  
        '''
        copied_val = self.val
        
        if isinstance(self.val,dict):
            copied_val = {}
            for key in self.val.keys():
                copied_val[key] = self.val[key]
        elif isinstance(self.val,list):
            copied_val = []
            for element in self.val:
                copied_val.append(element)

        return copied_val


    def update_version_and_val(
        self,invalid_listener,version_obj,val):
        '''
        @param {_ReferenceVersion} version_obj 
        @param {Anything} val
        
        If we are a peered variable, then when the other side makes a
        change, we want to update the dirty version of our object and
        resume from there.  To do this, just overwrite the dirty
        element's version_obj + val.
        '''

        # FIXME: eventually, want to transmit deltas instead of the
        # full val and version_obj.  
        if not self.peered:
            util.logger_assert(
                'Should not be updating value and version for a ' +
                'non-peered data item.')
        
        self._lock()
        self._add_invalid_listener(invalid_listener)
        dirty_element = self._dirty_map[invalid_listener.uuid]
        dirty_element.set_version_obj_and_val(version_obj,val)
        
        self._unlock()

        
    def _add_invalid_listener(self,invalid_listener):
        '''
        ASSUMES ALREADY WITHIN LOCK
        '''
        if invalid_listener.uuid not in self._dirty_map:
            
            # FIXME: may only want to make a copy of val on write
            to_add = self.dirty_element_constructor(
                self.version_obj.copy(),
                self.val,
                invalid_listener)
            
            self._dirty_map[invalid_listener.uuid] = to_add
            invalid_listener.add_touch(self)

    def get_val(self,invalid_listener):
        '''
        Requests a copy of the internal 
        '''
        self._lock()
        self._add_invalid_listener(invalid_listener)
        dirty_val = self._dirty_map[invalid_listener.uuid].val
        self._unlock()
        return dirty_val
    

    def write_val(self,invalid_listener,new_val):
        '''
        Writes to a copy of internal val, dirtying it
        '''
        self._lock()
        self._add_invalid_listener(invalid_listener)
        self._dirty_map[invalid_listener.uuid].set_has_been_written_to(new_val)
        self._unlock()
        

    def check_commit_hold_lock(self,invalid_listener):
        '''
        @returns{bool} --- Returns True if the commit associated with
        invalid_listener can go through (ie, no one else has committed
        to this waldo object since we read/wrote our dirty values.
        False otherwise.

        Note: takes lock on object, but does not release it.  Lock
        gets unreleased either within commit or release.
        '''
        self._lock()

        #### DEBUG
        if invalid_listener.uuid not in self._dirty_map:
            util.logger_assert('Aborted in check_commit_hold_lock.  ' +
                               'Have no listener in dirty map with ' +
                               'appropriate id.')
        #### END DEBUG

        return not self.version_obj.conflicts(
            self._dirty_map[invalid_listener.uuid].version_obj)


    
    def backout(self,invalid_listener,release_lock_after):
        '''
        @param {_InvalidListener} invalid_listener ---

        @param {bool} release_lock_after --- If true, then it means
        that the invalid_listener that called in was holding a commit
        lock on the object.  We should release that commit lock
        afterwards.
        '''
        if not release_lock_after:
            self._lock()
        
        #### DEBUG
        if invalid_listener.uuid not in self._dirty_map:
            util.logger_assert('Aborted in backout.  ' +
                               'Have no listener in dirty map with ' +
                               'appropriate id.')
        #### END DEBUG
            
        del self._dirty_map[invalid_listener.uuid]

        self._unlock()
            
    
    def complete_commit(self,invalid_listener):
        '''
        @param {_InvalidListener} invalid_listener --- The event that
        is committing the change.
        
        Assumes already inside of lock.  (Was presumably acquired in
        check_commit_hold_lock.

        Called when committing an invalid_listener's event.  

        If the invalid listener has only read the value (ie, the dirty
        map element associated with invalid_listener's uuid has a
        has_been_written_to of false), then make no change.

        If the invalid listener has modified val, then change val and
        increment the version number of the variable.  Additionally,
        run through all invalidation elements notifying them that
        their version numbers may be out of sync.

        In either case, remove the dirty map element associated with
        invalid_listener and release the lock.
        '''
        #### DEBUG
        if invalid_listener.uuid not in self._dirty_map:
            util.logger_assert('Aborted in commit.  ' +
                               'Have no listener in dirty map with ' +
                               'appropriate id.')
        #### END DEBUG


        dirty_map_elem  = self._dirty_map[invalid_listener.uuid]
        del self._dirty_map[invalid_listener.uuid]

        # will update version obj as well
        dirty_map_elem.update_obj_val_and_version(self)

        # determine who we need to send invalidation messages to
        to_invalidate_list = []
        for potentially_invalidate in list(self._dirty_map.values()):
            if potentially_invalidate.version_obj.conflicts(
                self.version_obj):
                to_invalidate_list.append(potentially_invalidate)


        # FIXME: May eventually want to send what the conflict was so
        # can determine how much the invalidation listener actually
        # needs to backout.
        if len(to_invalidate_list) != 0:
            dirty_notify_thread = _DirtyNotifyThread(
                self,to_invalidate_list)
            dirty_notify_thread.start()
            
        self._unlock()



class _DirtyNotifyThread(threading.Thread):
    '''
    When we commit a change to a Waldo object, notify all
    invalidation_listeners (essentially, events) of the change so that
    they can restart themselves accordingly.
    '''
    
    def __init__(self,wld_obj,to_notify_list):
        '''
        @param {_WaldoObj} wld_obj --- Who is notifying you that you
        are out of date.
        
        @param {List<DirtyMapElements>} to_notify_list --- Notify
        each of these invalid iterators that they are operating on an
        out-of-date value of the Waldo object, wld_obj.
        '''
        self.wld_obj = wld_obj
        self.to_notify_list = to_notify_list
        threading.Thread.__init__(self)
        self.daemon = True
        
    def run(self):
        for dirty_map_elem in self.to_notify_list:
            inv_listener = dirty_map_elem.invalidation_listener
            inv_listener.notify_invalidated(self.wld_obj)


            
class _DirtyMapElement(object):
    '''
    Each _WaldoObj holds a dirty map.  Its elements are of type
    _DirtyMapElement.  
    '''
    
    def __init__(self,version_obj,val,invalidation_listener):
        '''
        @param {_WaldoObjVersion} version_obj --- The version of the
        Waldo object that the dirty map element

        @param {Anything} val --- The dirty val that the invalidation
        listener is using.

        @param {_InvalidationListener} invalidation_listener --- 
        '''
        self.version_obj = version_obj
        self.val = val
        self.invalidation_listener = invalidation_listener

        
    def set_version_obj_and_val(self,version_obj,val):
        '''
        @see update_version_and_val in _ReferenceBase.
        '''
        self.version_obj = version_obj
        self.val = val

    def set_has_been_written_to(self,new_val):
        self.version_obj.set_has_been_written_to()
        self.val = new_val

    def update_obj_val_and_version(self,w_obj):
        '''
        @param {_WaldoObject} w_obj --- Take our version object and
        determine if we need to update w_obj's val and version.  This
        already assumes that DirtyMapElement has already had no commit
        conflict and is in the process of committing.  Similarly, we
        are already inside of w_obj's internal lock.
        '''
        self.version_obj.update_obj_val_and_version(w_obj,self.val)

        

class _ReferenceVersion(object):
    '''
    To keep track of whether an object is dirty, each WaldoObj holds a
    _WaldoOjbVersion object.  Using its methods, can automatically
    determine if an update from a dirtyElement will apply cleanly, or
    need to be backed out.
    '''
    
    @abstractmethod
    def copy(self):
        '''
        Whenever we create a dirty element, we create a new
        WaldoObjVersion.  This is used to check whether there might be
        any conflicts when trying to commit an event, using the
        conflicts method.
        '''
        pass

    @abstractmethod
    def update(self,dirty_version_obj):
        '''
        @param{_WaldoObjVersion} dirty_version_obj --- Commit the
        version held by dirty_version_obj to self.  (Assumes already
        has called conflicts to determine that there was no conflict
        from applying the new version.)
        '''
        pass

    @abstractmethod
    def conflicts(self,dirty_version_obj):
        '''
        @param{_WaldoObjVersion} dirty_version_obj
        
        @returns {bool} --- True if the there would be a read-write
        conflict from attempting to commit the event with
        dirty_version_obj on top of this version obj.
        '''
        pass

    @abstractmethod
    def update_obj_val_and_version(self,w_obj,val):
        '''
        @param {_WaldoObject} w_obj --- Take our version object and
        determine if we need to update w_obj's val and version.  This
        already assumes that DirtyMapElement has already had no commit
        conflict and is in the process of committing.  Similarly, we
        are already inside of w_obj's internal lock.

        @param {Anything} val --- What the dirtyelementobject thinks
        the current value of the object should be.
        '''
        pass


    def serializable_for_network_data(self):
        '''
        The dirty map's version object must be serialized and passed
        to the partner endpoint for deserialization so that the
        partner endpoint knows which fields were changed on
        serializer's side.
        '''

        # FIXME: Lots of overhead in pickling entire class instead of
        # just the necessary data.
        return pickle.dumps(self)

    @staticmethod
    def deserialize_version_obj_from_network_data(
        version_network_data):
        '''
        @param {Currently string} version_network_data --- The result
        of a call to serilizable_for_network_data on a version object.
        '''
        return pickle.loads(version_network_data)
        

    
    

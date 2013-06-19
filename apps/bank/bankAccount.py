# Waldo emitted file


def Account (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Account (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,initial_balance,in_acct_id):

            # a little ugly in that need to pre-initialize _host_uuid, because
            # code used for initializing variable store may rely on it.  (Eg., if
            # initializing nested lists.)
            self._waldo_classes = _waldo_classes
            self._host_uuid = _host_uuid
            self._global_var_store = self._waldo_classes["VariableStore"](_host_uuid)
            _active_event = None
            _context = self._waldo_classes["ExecutingEventContext"](
                self._global_var_store,
                # not using sequence local store
                self._waldo_classes["VariableStore"](_host_uuid))

            self._global_var_store.add_var(
                '0__balance',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '0__balance', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '1__acct_id',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '1__acct_id', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)


            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._onCreate(_root_event,_ctx ,initial_balance,in_acct_id,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done

                    # local endpoint's initialization has succeeded, tell other side that
                    # we're done initializing.
                    self._this_side_ready()

                    return _to_return

                
            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        def _onCreate(self,_active_event,_context,initial_balance,in_acct_id,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                initial_balance = _context.turn_into_waldo_var_if_was_var(initial_balance,True,_active_event,self._host_uuid,False)
                in_acct_id = _context.turn_into_waldo_var_if_was_var(in_acct_id,True,_active_event,self._host_uuid,False)

                pass

            else:
                initial_balance = _context.turn_into_waldo_var_if_was_var(initial_balance,True,_active_event,self._host_uuid,False)
                in_acct_id = _context.turn_into_waldo_var_if_was_var(in_acct_id,True,_active_event,self._host_uuid,False)

                pass

            _tmp0 = initial_balance
            if not _context.assign(_context.global_store.get_var_if_exists("0__balance"),_tmp0,_active_event):
                pass

            _tmp0 = in_acct_id
            if not _context.assign(_context.global_store.get_var_if_exists("1__acct_id"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def get_balance(self):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__get_balance(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__get_balance(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("0__balance") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("0__balance"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("0__balance"))




        def set_balance(self,new_value):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__set_balance(_root_event,_ctx ,new_value,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__set_balance(self,_active_event,_context,new_value,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                new_value = _context.turn_into_waldo_var_if_was_var(new_value,True,_active_event,self._host_uuid,False)

                pass

            else:
                new_value = _context.turn_into_waldo_var_if_was_var(new_value,True,_active_event,self._host_uuid,False)

                pass

            _tmp0 = new_value
            if not _context.assign(_context.global_store.get_var_if_exists("0__balance"),_tmp0,_active_event):
                pass



        def get_id(self):

            # ensure that both sides have completed their onCreate calls
            # before continuing
            self._block_ready()

            while True:  # FIXME: currently using infinite retry 
                _root_event = self._act_event_map.create_root_event()
                _ctx = self._waldo_classes["ExecutingEventContext"](
                    self._global_var_store,
                    # not using sequence local store
                    self._waldo_classes["VariableStore"](self._host_uuid))

                # call internal function... note True as last param tells internal
                # version of function that it needs to de-waldo-ify all return
                # arguments (while inside transaction) so that this method may
                # return them....if it were false, might just get back refrences
                # to Waldo variables, and de-waldo-ifying them outside of the
                # transaction might return over-written/inconsistent values.
                _to_return = self._endpoint_func_call_prefix__waldo__get_id(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__get_id(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__acct_id") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("1__acct_id"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__acct_id"))



        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return _Account(_waldo_classes,_host_uuid,_conn_obj,*args)
def _Account (_waldo_classes,_host_uuid,_conn_obj,*args):
    class __Account (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj):

            # a little ugly in that need to pre-initialize _host_uuid, because
            # code used for initializing variable store may rely on it.  (Eg., if
            # initializing nested lists.)
            self._waldo_classes = _waldo_classes
            self._host_uuid = _host_uuid
            self._global_var_store = self._waldo_classes["VariableStore"](_host_uuid)
            _active_event = None
            _context = self._waldo_classes["ExecutingEventContext"](
                self._global_var_store,
                # not using sequence local store
                self._waldo_classes["VariableStore"](_host_uuid))

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)



            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        # no oncreate defined to emit method for 
        ### USER DEFINED METHODS ###
        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return __Account(_waldo_classes,_host_uuid,_conn_obj,*args)

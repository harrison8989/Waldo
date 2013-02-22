import threading
import Queue
import util
import waldoServiceActions
import pickle
import waldoActiveEventMap
import waldoMessages

class _EndpointServiceThread(threading.Thread):
    def __init__(self,endpoint):
        '''
        @param {_Endpoint object} endpoint
        '''
        self.endpoint = endpoint

        # each element is an _Action (@see
        # waldoServiceActions._Action).
        self.threadsafe_queue = Queue.Queue()        
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        '''
        Event loop.  Keep on reading off queue and servicing.
        '''
        while True:
            service_action = self.threadsafe_queue.get()
            service_action.service()

    def receive_request_backout(self,uuid,requesting_endpoint):
        '''
        @param {uuid} uuid --- The uuid of the _ActiveEvent that we
        want to backout.

        @param {either Endpoint object or
        util.PARTNER_ENDPOINT_SENTINEL} requesting_endpoint ---
        Endpoint object if was requested to backout by endpoint objects
        on this same host (from endpoint object calls).
        util.PARTNER_ENDPOINT_SENTINEL if was requested to backout
        by partner.
        
        Called by another endpoint on this endpoint (not called by
        external non-Waldo code).
        '''
        req_backout_action = waldoServiceActions._ReceiveRequestBackoutAction(
            self.endpoint,uuid,requesting_endpoint)
        self.threadsafe_queue.put(req_backout_action)
        

    def receive_request_complete_commit(self,event_uuid,request_from_partner):
        '''
        Another endpoint (either on the same host as I am or my
        partner) asked me to complete the second phase of the commit
        for an event with uuid event_uuid.
        
        @param {uuid} event_uuid --- The uuid of the event we are
        trying to commit.

        @param {bool} request_from_partner --- True if the request to
        complete the commit came from my partner, false otherwise (the
        request came from an endpoint on the same host as I am)
        '''
        req_complete_commit_action = (
            waldoServiceActions._ReceiveRequestCompleteCommitAction(
                self.endpoint,event_uuid,request_from_partner))
        
        self.threadsafe_queue.put(req_complete_commit_action)

    def receive_endpoint_call(
        self,endpoint_making_call,event_uuid,func_name,result_queue,*args):
        '''
        @param{_Endpoint object} endpoint_making_call --- The endpoint
        that made the endpoint call into this endpoint.

        @param {uuid} event_uuid --- 

        @param {string} func_name --- The name of the Public function
        to execute (in the Waldo source file).

        @param {Queue.Queue} result_queue --- When the function
        returns, wrap it in a
        waldoEndpointCallResult._EndpointCallResult object and put it
        into this threadsafe queue.  The endpoint that made the call
        is blocking waiting for the result of the call. 

        @param {*args} *args --- additional arguments that the
        function requires.

        Called by another endpoint on this endpoint (not called by
        external non-Waldo code).
        '''
        endpt_call_action = waldoServiceActions._ReceiveEndpointCallAction(
            self.endpoint,endpoint_making_call,event_uuid,func_name,
            result_queue,*args)
        self.threadsafe_queue.put(req_backout_action)

    def receive_partner_request_commit(self,msg):
        '''
        @param {_PartnerCommitRequestMessage} msg
        '''
        partner_request_commit_action = (
            waldoServiceActions._ReceivePartnerRequestCommitAction(
                self.endpoint,msg.event_uuid))
        self.threadsafe_queue.put(partner_request_commit_action)

    def receive_partner_request_complete_commit(self,msg):
        '''
        @param {_PartnerCommitRequestMessage} msg
        '''
        partner_request_complete_commit_action = (
            waldoServiceActions._ReceiveRequestCompleteCommitAction(
                self.endpoint,msg.event_uuid,True))
        self.threadsafe_queue.put(partner_request_complete_commit_action)

        
    def receive_partner_request_message_sequence_block(self,msg):
        '''
        @param {_PartnerRequestSequenceBlockMessage} msg --- Contains
        all the information for the request partner made.
        '''
        partner_request_sequence_block_action = (
            waldoServiceActions._ReceivePartnerMessageRequestSequenceBlockAction(
                self.endpoint,msg))
            
        self.threadsafe_queue.put(partner_request_sequence_block_action)

    def receive_request_commit_from_endpoint(self,uuid,requesting_endpoint):
        '''
        @param {uuid} uuid --- The uuid of the _ActiveEvent that we
        want to commit.

        @param {Endponit object} requesting_endpoint --- 
        Endpoint object if was requested to commit by endpoint objects
        on this same host (from endpoint object calls).

        
        Called by another endpoint on this endpoint (not called by
        external non-Waldo code).

        Forward the commit request to any other endpoints that were
        touched when the event was processed on this side.
        '''

        # the below code is copied from partner.  should use different
        # version for local.
        # partner_request_commit_action = (
        #     waldoServiceActions._ReceivePartnerRequestCommitAction(
        #         self.endpoint,msg.event_uuid))
        # self.threadsafe_queue.put(partner_request_commit_action)

        util.logger_assert(
            'Must finish code for receive_request_commit in service thread')


class _Endpoint(object):
    '''
    All methods that begin with _receive, are called by other
    endpoints or from connection object's receiving a message from
    partner endpoint.

    All methods that begin with _forward or _send are called from
    active events on this endpoint.
    '''
    
    def __init__(self,commit_manager,conn_obj,global_var_store):
        '''
        @param {_CommitManager} commit_manager
        
        @param {ConnectionObject} conn_obj --- Used to write messages
        to partner endpoint.

        @param {_VariableStore} global_var_store --- Contains the
        peered and endpoint global data for this endpoint.  Will not
        add or remove any peered or endpoint global variables.  Will
        only make calls on them.
        '''
        self._act_event_map = waldoActiveEventMap._ActiveEventMap(commit_manager,self)
        self._conn_obj = conn_obj

        # whenever we create a new _ExecutingEvent, we point it at
        # this variable store so that it knows where it can retrieve
        # variables.
        self._global_var_store = global_var_store

        self._commit_manager = commit_manager

        self._endpoint_service_thread = _EndpointServiceThread(self)
        self._endpoint_service_thread.start()
        
    def _request_commit(self,uuid,requesting_endpoint):
        '''
        @see _EndpointServiceThread.request_commit
        '''
        self._endpoint_service_thread.request_commit(
            uuid,requesting_endpoint)

    def _receive_request_backout(self,uuid,requesting_endpoint):
        '''
        @see _EndpointServiceThread.receive_request_backout
        '''
        self._endpoint_service_thread.receive_request_backout(
            uuid,requesting_endpoint)

    def _receive_request_commit(self,uuid,requesting_endpoint):
        '''
        Called by another endpoint on the same host as this endpoint
        to begin the first phase of the commit of the active event
        with uuid "uuid."
        '''
        self._endpoint_service_thread.receive_request_commit_from_endpoint(
            uuid,requesting_endpoint)
        
    def _receive_request_complete_commit(self,uuid):
        '''
        Called by another endpoint on the same host as this endpoint
        to finish the second phase of the commit of active event with
        uuid "uuid."
        '''
        self._endpoint_service_thread.receive_request_complete_commit(
            uuid,
            False # complete commit request was not from partner
                  # endpoint.
            )

    def _receive_msg_from_partner(self,string_msg):
        '''
        Called by the connection object.

        @param {String} string_msg --- A raw byte string sent from
        partner.  Should be able to deserialize it, convert it into a
        message, and dispatch it as an event.

        Can receive a variety of messages from partner: request to
        execute a sequence block, request to commit a change to a
        peered variable, request to backout an event, etc.  In this
        function, we dispatch depending on message we receive.
        '''
        
        msg_map = pickle.loads(string_msg)
        msg = waldoMessages._Message.map_to_msg(msg_map)
        
        if isinstance(msg,waldoMessages._PartnerRequestSequenceBlockMessage):
            self._endpoint_service_thread.receive_partner_request_message_sequence_block(
                msg)
        elif isinstance(msg,waldoMessages._PartnerCommitRequestMessage):
            self._endpoint_service_thread.receive_partner_request_commit(msg)
        elif isinstance(msg,waldoMessages._PartnerCompleteCommitRequestMessage):
            self._endpoint_service_thread.receive_partner_request_complete_commit(msg)
        else:
            #### DEBUG
            util.logger_assert(
                'Do not know how to convert message to event action ' +
                'in _receive_msg_from_partner.')
            #### END DEBUG

            
    def _receive_endpoint_call(
        self,endpoint_making_call,event_uuid,func_name,result_queue,*args):
        '''
        For params, @see _EndpointServiceThread.endpoint_call
        
        Non-blocking.  Requests the endpoint_service_thread to perform
        the endpoint function call listed as
        '''
        self._endpoint_service_thread.receive_endpoint_call(
            endpoint_making_call,event_uuid,func_name,result_queue,*args)


    def _send_partner_message_sequence_block_request(
        self,block_name,event_uuid,reply_with_uuid,reply_to_uuid,
        invalidation_listener,sequence_local_store):
        '''
        Sends a message using connection object to the partner
        endpoint requesting it to perform some message sequence
        action.
        
        @param {String} block_name --- The name of the sequence block
        we want to execute on the partner endpoint. (Note: this is how
        that sequence block is named in the source Waldo file, not how
        it is translated by the compiler into a function.

        @param {uuid} event_uuid --- The uuid of the requesting event.

        @param {uuid} reply_with_uuid --- When the partner endpoint
        responds, it should place reply_with_uuid in its reply_to
        message field.  That way, we can determine which message the
        partner endpoint was replying to.

        @param {uuid or None} reply_to_uuid --- If this is the
        beginning of a sequence of messages, then fill the reply_to
        field of the message with None (the message is not a reply to
        anything that we have seen so far).  Otherwise, put the
        reply_with message field of the last message that the partner
        said as part of this sequence in.

        @param {_InvalidationListener} invalidation_listener --- The
        invalidation listener that is requesting the message to be
        sent.

        @param {_VariableStore} sequence_local_store --- We convert
        all changes that we have made to both peered data and sequence
        local data to maps of deltas so that the partner endpoint can
        apply the changes.  We use the sequence_local_store to get
        changes that invalidation_listener has made to sequence local
        data.  (For peered data, we can just use
        self._global_var_store.)
        
        '''
        # FIXME: need to get data_contents from invalidation_listener.
        # should contain the peered data that has been written to.

        glob_deltas = self._global_var_store.generate_deltas(
            invalidation_listener)
        sequence_local_deltas = sequence_local_store.generate_deltas(
            invalidation_listener)
        
        msg_to_send = waldoMessages._PartnerRequestSequenceBlockMessage(
            event_uuid,block_name,reply_with_uuid,reply_to_uuid,
            glob_deltas,sequence_local_deltas)

        msg_map = msg_to_send.msg_to_map()

        self._conn_obj.write(pickle.dumps(msg_map),self)

        
    def _forward_commit_request_partner(self,active_event):
        '''
        @param {_ActiveEvent} active_event --- Has the same uuid as
        the event we will forward a commit to our partner for.
        '''
        # FIXME: may be a way to piggyback commit with final event in
        # sequence.

        msg = waldoMessages._PartnerCommitRequestMessage(active_event.uuid)
        msg_map = msg.msg_to_map()
        self._conn_obj.write(pickle.dumps(msg_map),self)
        

    def _forward_complete_commit_request_partner(self,active_event):
        '''
        Active event on this endpoint has completed its commit and it
        wants you to tell partner endpoint as well to complete its
        commit.
        '''
        msg = waldoMessages._PartnerCompleteCommitRequestMessage(active_event.uuid)
        msg_map = msg.msg_to_map()
        self._conn_obj.write(pickle.dumps(msg_map),self)

        
    def _forward_backout_request_partner(self,active_event):
        '''
        @param {_ActiveEvent} active_event --- Has the same uuid as
        the event we will forward a backout request to our partner
        for.
        '''
        util.logger_assert(
            'Call to unfinished _forward_backout_request_partner in ' +
            '_Endpoint.')
        
        # FIXME: fill this in ... use self._conn_obj


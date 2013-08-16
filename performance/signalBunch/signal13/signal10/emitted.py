# Waldo emitted file


def Server (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Server (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,init_display_msg_func,init_nothing_func):

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
                '0__glob',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '0__glob', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '1__display_msg_func',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '1__display_msg_func', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ).set_external_args_array([]))

            self._global_var_store.add_var(
                '2__nothing_func',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '2__nothing_func', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ).set_external_args_array([]))

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
                try:
                    _to_return = self._onCreate(_root_event,_ctx ,init_display_msg_func,init_nothing_func,[])
                except self._waldo_classes["BackoutException"]:
                    pass

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

        def _onCreate(self,_active_event,_context,init_display_msg_func,init_nothing_func,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[],False)
                init_nothing_func = _context.func_turn_into_waldo_var(init_nothing_func,True,_active_event,self._host_uuid,False,[],False)

                pass

            else:
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[],False)
                init_nothing_func = _context.func_turn_into_waldo_var(init_nothing_func,True,_active_event,self._host_uuid,False,[],False)

                pass

            _tmp0 = init_display_msg_func
            if not _context.assign(_context.global_store.get_var_if_exists("1__display_msg_func"),_tmp0,_active_event):
                pass

            _tmp0 = init_nothing_func
            if not _context.assign(_context.global_store.get_var_if_exists("2__nothing_func"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def sendMSG(self,msg,num):

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
                try:
                    _to_return = self._endpoint_func_call_prefix__waldo__sendMSG(_root_event,_ctx ,msg,num,[])
                except self._waldo_classes["BackoutException"]:
                    pass

                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__sendMSG(self,_active_event,_context,msg,num,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False,False)
                num = _context.turn_into_waldo_var_if_was_var(num,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False,False)
                num = _context.turn_into_waldo_var_if_was_var(num,True,_active_event,self._host_uuid,False,False)

                pass

            _context.signal_call(_active_event,_context.global_store.get_var_if_exists("1__display_msg_func"),msg,)

            n = 0
            for _secret_waldo_for_iter____n in _context.get_for_iter(self._waldo_classes["WaldoSingleThreadListVariable"]("garbage",self._host_uuid,False,list(range(_context.get_val_if_waldo(0 ,_active_event),_context.get_val_if_waldo(num,_active_event),_context.get_val_if_waldo(1 ,_active_event)))),_active_event):
                n = _context.write_val(n,_secret_waldo_for_iter____n,_active_event)

                pass



        def nothing(self):

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
                try:
                    _to_return = self._endpoint_func_call_prefix__waldo__nothing(_root_event,_ctx ,[])
                except self._waldo_classes["BackoutException"]:
                    pass

                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__nothing(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return _Server(_waldo_classes,_host_uuid,_conn_obj,*args)
def _Server (_waldo_classes,_host_uuid,_conn_obj,*args):
    class __Server (_waldo_classes["Endpoint"]):
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

    return __Server(_waldo_classes,_host_uuid,_conn_obj,*args)

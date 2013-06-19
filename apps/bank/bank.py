# Waldo emitted file


def Bank (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Bank (_waldo_classes["Endpoint"]):
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

            self._global_var_store.add_var(
                '0__all_endpoints',self._waldo_classes["WaldoMapVariable"](  # the type of waldo variable to create
                '0__all_endpoints', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._waldo_classes["Endpoint"].__init__(self,_waldo_classes,_host_uuid,_conn_obj,self._global_var_store)



            # local endpoint's initialization has succeeded, tell other side that
            # we're done initializing.
            self._this_side_ready()


        ### OnCreate method

        # no oncreate defined to emit method for 
        ### USER DEFINED METHODS ###

        def add_endpoint(self,endpt):

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
                _to_return = self._endpoint_func_call_prefix__waldo__add_endpoint(_root_event,_ctx ,endpt,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__add_endpoint(self,_active_event,_context,endpt,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                endpt = _context.turn_into_waldo_var_if_was_var(endpt,True,_active_event,self._host_uuid,False)

                pass

            else:
                endpt = _context.turn_into_waldo_var_if_was_var(endpt,True,_active_event,self._host_uuid,False)

                pass

            id = _context.get_val_if_waldo(_context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(endpt,_active_event),"get_id",),_active_event)
            _tmp0 = endpt
            _context.assign_on_key(_context.global_store.get_var_if_exists("0__all_endpoints"),id,_tmp0, _active_event)



        def total_money_held(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__total_money_held(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__total_money_held(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            total_balance = _context.get_val_if_waldo(0 ,_active_event)
            key = 0
            for _secret_waldo_for_iter____key in _context.get_for_iter(_context.global_store.get_var_if_exists("0__all_endpoints"),_active_event):
                key = _context.write_val(key,_secret_waldo_for_iter____key,_active_event)
                endpt = self._waldo_classes["WaldoEndpointVariable"](  # the type of waldo variable to create
                    '5__endpt', # variable's name
                    self._host_uuid, # host uuid var name
                    False,  # if peered, True, otherwise, False
                    _context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__all_endpoints").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(key,_active_event)),_active_event)
                )
                _tmp0 = (_context.get_val_if_waldo(total_balance,_active_event) + _context.get_val_if_waldo(_context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(endpt,_active_event),"get_balance",),_active_event))
                if not _context.assign(total_balance,_tmp0,_active_event):
                    total_balance = _tmp0


                pass



        def transfer_money(self,from_id,to_id,amount):

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
                _to_return = self._endpoint_func_call_prefix__waldo__transfer_money(_root_event,_ctx ,from_id,to_id,amount,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__transfer_money(self,_active_event,_context,from_id,to_id,amount,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                from_id = _context.turn_into_waldo_var_if_was_var(from_id,True,_active_event,self._host_uuid,False)
                to_id = _context.turn_into_waldo_var_if_was_var(to_id,True,_active_event,self._host_uuid,False)
                amount = _context.turn_into_waldo_var_if_was_var(amount,True,_active_event,self._host_uuid,False)

                pass

            else:
                from_id = _context.turn_into_waldo_var_if_was_var(from_id,True,_active_event,self._host_uuid,False)
                to_id = _context.turn_into_waldo_var_if_was_var(to_id,True,_active_event,self._host_uuid,False)
                amount = _context.turn_into_waldo_var_if_was_var(amount,True,_active_event,self._host_uuid,False)

                pass

            if _context.get_val_if_waldo((_context.get_val_if_waldo(( not ( _context.get_val_if_waldo(_context.handle_in_check(from_id,_context.global_store.get_var_if_exists("0__all_endpoints"),_active_event),_active_event) )),_active_event) or _context.get_val_if_waldo(( not ( _context.get_val_if_waldo(_context.handle_in_check(to_id,_context.global_store.get_var_if_exists("0__all_endpoints"),_active_event),_active_event) )),_active_event)),_active_event):

                if _returning_to_public_ext_array != None:
                    # must de-waldo-ify objects before passing back
                    return _context.flatten_into_single_return_tuple(False  if 0 in _returning_to_public_ext_array else _context.de_waldoify(False ,_active_event))


                # otherwise, use regular return mechanism... do not de-waldo-ify
                return _context.flatten_into_single_return_tuple(False )



                pass


            from_endpoint = self._waldo_classes["WaldoEndpointVariable"](  # the type of waldo variable to create
                '10__from_endpoint', # variable's name
                self._host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__all_endpoints").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(from_id,_active_event)),_active_event)
            )
            if _context.get_val_if_waldo((_context.get_val_if_waldo(amount,_active_event) > _context.get_val_if_waldo(_context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(from_endpoint,_active_event),"get_balance",),_active_event)),_active_event):

                if _returning_to_public_ext_array != None:
                    # must de-waldo-ify objects before passing back
                    return _context.flatten_into_single_return_tuple(False  if 0 in _returning_to_public_ext_array else _context.de_waldoify(False ,_active_event))


                # otherwise, use regular return mechanism... do not de-waldo-ify
                return _context.flatten_into_single_return_tuple(False )



                pass


            to_endpoint = self._waldo_classes["WaldoEndpointVariable"](  # the type of waldo variable to create
                '12__to_endpoint', # variable's name
                self._host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(_context.global_store.get_var_if_exists("0__all_endpoints").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(to_id,_active_event)),_active_event)
            )
            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(from_endpoint,_active_event),"set_balance",(_context.get_val_if_waldo(_context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(from_endpoint,_active_event),"get_balance",),_active_event) - _context.get_val_if_waldo(amount,_active_event)),)
            _context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(to_endpoint,_active_event),"set_balance",(_context.get_val_if_waldo(_context.hide_endpoint_call(_active_event,_context,_context.get_val_if_waldo(to_endpoint,_active_event),"get_balance",),_active_event) + _context.get_val_if_waldo(amount,_active_event)),)

            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(True  if 0 in _returning_to_public_ext_array else _context.de_waldoify(True ,_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(True )



        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

    return _Bank(_waldo_classes,_host_uuid,_conn_obj,*args)
def _Bank (_waldo_classes,_host_uuid,_conn_obj,*args):
    class __Bank (_waldo_classes["Endpoint"]):
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

    return __Bank(_waldo_classes,_host_uuid,_conn_obj,*args)

# Waldo emitted file


def Client (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Client (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,init_display_msg_func):

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
                '0__random',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '0__random', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(1299321 ,_active_event)
            ))

            self._global_var_store.add_var(
                '1__key',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '1__key', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(2401 ,_active_event)
            ))

            self._global_var_store.add_var(
                '2__cipherList',self._waldo_classes["WaldoListVariable"](  # the type of waldo variable to create
                '2__cipherList', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(self._waldo_classes["WaldoListVariable"]("garbage_name",
                self._host_uuid,
                False,
                ['cipherwon' ,'ciphertoo' ,]),_active_event)
            ))

            self._global_var_store.add_var(
                '3__compressList',self._waldo_classes["WaldoListVariable"](  # the type of waldo variable to create
                '3__compressList', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(self._waldo_classes["WaldoListVariable"]("garbage_name",
                self._host_uuid,
                False,
                ['compresswon' ,'compresstoo' ,]),_active_event)
            ))

            self._global_var_store.add_var(
                '4__display_msg_func',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '4__display_msg_func', # variable's name
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
                _to_return = self._onCreate(_root_event,_ctx ,init_display_msg_func,[])
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

        def _onCreate(self,_active_event,_context,init_display_msg_func,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[])

                pass

            else:
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[])

                pass

            _tmp0 = init_display_msg_func
            if not _context.assign(_context.global_store.get_var_if_exists("4__display_msg_func"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def send_msg(self,msg):

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
                _to_return = self._endpoint_func_call_prefix__waldo__send_msg(_root_event,_ctx ,msg,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__send_msg(self,_active_event,_context,msg,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False)

                pass

            else:
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False)

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__SeqSendMsg(_active_event,_context,msg,) if _context.set_msg_send_initialized_bit_false() else None)


        def startSeq(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__startSeq(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__startSeq(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple((self._partner_endpoint_msg_func_call_prefix__waldo__HandshakeSeq(_active_event,_context,1.1 ,_context.global_store.get_var_if_exists("2__cipherList"),_context.global_store.get_var_if_exists("3__compressList"),) if _context.set_msg_send_initialized_bit_false() else None) if 0 in _returning_to_public_ext_array else _context.de_waldoify((self._partner_endpoint_msg_func_call_prefix__waldo__HandshakeSeq(_active_event,_context,1.1 ,_context.global_store.get_var_if_exists("2__cipherList"),_context.global_store.get_var_if_exists("3__compressList"),) if _context.set_msg_send_initialized_bit_false() else None),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple((self._partner_endpoint_msg_func_call_prefix__waldo__HandshakeSeq(_active_event,_context,1.1 ,_context.global_store.get_var_if_exists("2__cipherList"),_context.global_store.get_var_if_exists("3__compressList"),) if _context.set_msg_send_initialized_bit_false() else None))



        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__HandshakeSeq(self,_active_event,_context,TLS=None,cipher=None,compress=None,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    _context.sequence_local_store.add_var(
                        "26__TLS", _context.convert_for_seq_local(TLS,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "27__cipher", _context.convert_for_seq_local(cipher,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "28__compress", _context.convert_for_seq_local(compress,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "26__TLS", _context.convert_for_seq_local(TLS,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "27__cipher", _context.convert_for_seq_local(cipher,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "28__compress", _context.convert_for_seq_local(compress,_active_event,self._host_uuid)
                    )

                    pass

                n = 0
                _context.sequence_local_store.add_var(
                    "17__n",_context.convert_for_seq_local(n,_active_event,self._host_uuid))
                rand = 0
                _context.sequence_local_store.add_var(
                    "18__rand",_context.convert_for_seq_local(rand,_active_event,self._host_uuid))
                myKey = 0
                _context.sequence_local_store.add_var(
                    "19__myKey",_context.convert_for_seq_local(myKey,_active_event,self._host_uuid))
                myCiph = ""
                _context.sequence_local_store.add_var(
                    "20__myCiph",_context.convert_for_seq_local(myCiph,_active_event,self._host_uuid))
                myComp = ""
                _context.sequence_local_store.add_var(
                    "21__myComp",_context.convert_for_seq_local(myComp,_active_event,self._host_uuid))
                certificate = ""
                _context.sequence_local_store.add_var(
                    "22__certificate",_context.convert_for_seq_local(certificate,_active_event,self._host_uuid))
                clientYes = _context.get_val_if_waldo(False ,_active_event)
                _context.sequence_local_store.add_var(
                    "23__clientYes",_context.convert_for_seq_local(clientYes,_active_event,self._host_uuid))
                serverYes = _context.get_val_if_waldo(False ,_active_event)
                _context.sequence_local_store.add_var(
                    "24__serverYes",_context.convert_for_seq_local(serverYes,_active_event,self._host_uuid))
                success = 0
                _context.sequence_local_store.add_var(
                    "29__success",_context.convert_for_seq_local(success,_active_event,self._host_uuid))

                pass

            _tmp0 = 0 
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("17__n"),_tmp0,_active_event):
                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'hello',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return _context.sequence_local_store.get_var_if_exists("29__success")

        def _partner_endpoint_msg_func_call_prefix__waldo__SeqSendMsg(self,_active_event,_context,msg=None,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    _context.sequence_local_store.add_var(
                        "33__msg", _context.convert_for_seq_local(msg,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "33__msg", _context.convert_for_seq_local(msg,_active_event,self._host_uuid)
                    )

                    pass


                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'receive',_threadsafe_queue, '_first_msg')
            _queue_elem = _threadsafe_queue.get()

            if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                raise self._waldo_classes["BackoutException"]()

            _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

            # apply changes to sequence variables.  (There shouldn't
            # be any, but it's worth getting in practice.)  Note: that
            # the system has already applied deltas for global data.
            _context.sequence_local_store.incorporate_deltas(
                _active_event,_queue_elem.sequence_local_var_store_deltas)

            # send more messages
            _to_exec_next = _queue_elem.to_exec_next_name_msg_field
            if _to_exec_next != None:
                # means that we do not have any additional functions to exec
                _to_exec = getattr(self,_to_exec_next)
                _to_exec(_active_event,_context)
            else:
                # end of sequence: reset to_reply_with_uuid in context.  we do
                # this so that if we go on to execute another message sequence
                # following this one, then the message sequence will be viewed as
                # a new message sequence, rather than the continuation of a
                # previous one.
                _context.reset_to_reply_with()


            return 

        ### User-defined message receive blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__verify(self,_active_event,_context,_returning_to_public_ext_array=None):

            if _context.get_val_if_waldo(_context.handle_in_check('lolz' ,_context.sequence_local_store.get_var_if_exists("22__certificate"),_active_event),_active_event):
                _tmp0 = (_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("17__n"),_active_event) + _context.get_val_if_waldo(100 ,_active_event))
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("17__n"),_tmp0,_active_event):
                    pass

                _tmp0 = _context.global_store.get_var_if_exists("0__random")
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("18__rand"),_tmp0,_active_event):
                    pass

                _tmp0 = _context.global_store.get_var_if_exists("1__key")
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("19__myKey"),_tmp0,_active_event):
                    pass

                _tmp0 = True 
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("23__clientYes"),_tmp0,_active_event):
                    pass


                pass





            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__complete",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__complete" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


    return _Client(_waldo_classes,_host_uuid,_conn_obj,*args)
def Server (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Server (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,init_display_msg_func):

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
                '10__t',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '10__t', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(1.1 ,_active_event)
            ))

            self._global_var_store.add_var(
                '11__ciph',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '11__ciph', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo('cipherwon' ,_active_event)
            ))

            self._global_var_store.add_var(
                '12__comp',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '12__comp', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo('compresstoo' ,_active_event)
            ))

            self._global_var_store.add_var(
                '13__cert',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '13__cert', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo('' ,_active_event)
            ))

            self._global_var_store.add_var(
                '14__display_msg_func',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '14__display_msg_func', # variable's name
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
                _to_return = self._onCreate(_root_event,_ctx ,init_display_msg_func,[])
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

        def _onCreate(self,_active_event,_context,init_display_msg_func,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[])

                pass

            else:
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[])

                pass

            _tmp0 = init_display_msg_func
            if not _context.assign(_context.global_store.get_var_if_exists("14__display_msg_func"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def setCert(self,c):

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
                _to_return = self._endpoint_func_call_prefix__waldo__setCert(_root_event,_ctx ,c,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return


        def _endpoint_func_call_prefix__waldo__setCert(self,_active_event,_context,c,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                c = _context.turn_into_waldo_var_if_was_var(c,True,_active_event,self._host_uuid,False)

                pass

            else:
                c = _context.turn_into_waldo_var_if_was_var(c,True,_active_event,self._host_uuid,False)

                pass

            _tmp0 = c
            if not _context.assign(_context.global_store.get_var_if_exists("13__cert"),_tmp0,_active_event):
                pass


        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__hello(self,_active_event,_context,_returning_to_public_ext_array=None):

            if _context.get_val_if_waldo(_context.handle_in_check(_context.global_store.get_var_if_exists("11__ciph"),_context.sequence_local_store.get_var_if_exists("27__cipher"),_active_event),_active_event):
                _tmp0 = _context.global_store.get_var_if_exists("11__ciph")
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("20__myCiph"),_tmp0,_active_event):
                    pass

                _tmp0 = (_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("17__n"),_active_event) + _context.get_val_if_waldo(1 ,_active_event))
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("17__n"),_tmp0,_active_event):
                    pass


                pass


            if _context.get_val_if_waldo(_context.handle_in_check(_context.global_store.get_var_if_exists("12__comp"),_context.sequence_local_store.get_var_if_exists("28__compress"),_active_event),_active_event):
                _tmp0 = _context.global_store.get_var_if_exists("12__comp")
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("21__myComp"),_tmp0,_active_event):
                    pass

                _tmp0 = (_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("17__n"),_active_event) + _context.get_val_if_waldo(10 ,_active_event))
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("17__n"),_tmp0,_active_event):
                    pass


                pass


            _tmp0 = _context.global_store.get_var_if_exists("13__cert")
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("22__certificate"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__verify",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__verify" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__complete(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = (_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("17__n"),_active_event) + _context.get_val_if_waldo(1000 ,_active_event))
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("17__n"),_tmp0,_active_event):
                pass

            _tmp0 = True 
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("24__serverYes"),_tmp0,_active_event):
                pass

            _tmp0 = _context.sequence_local_store.get_var_if_exists("17__n")
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("29__success"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


        def _partner_endpoint_msg_func_call_prefix__waldo__receive(self,_active_event,_context,_returning_to_public_ext_array=None):

            _context.signal_call(_active_event,_context.global_store.get_var_if_exists("14__display_msg_func"),_context.sequence_local_store.get_var_if_exists("33__msg"),)




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out
                    raise self._waldo_classes["BackoutException"]()

                _context.set_to_reply_with(_queue_elem.reply_with_msg_field)

                # apply changes to sequence variables.  Note: that
                # the system has already applied deltas for global data.
                _context.sequence_local_store.incorporate_deltas(
                    _active_event,_queue_elem.sequence_local_var_store_deltas)

                # send more messages
                _to_exec_next = _queue_elem.to_exec_next_name_msg_field
                if _to_exec_next != None:
                    # means that we do not have any additional functions to exec
                    _to_exec = getattr(self,_to_exec_next)
                    _to_exec(_active_event,_context)


    return _Server(_waldo_classes,_host_uuid,_conn_obj,*args)

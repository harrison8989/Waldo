# Waldo emitted file


def Client (_waldo_classes,_host_uuid,_conn_obj,*args):
    class _Client (_waldo_classes["Endpoint"]):
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,init_get_MSG,n):

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
                '0__currGame',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '0__currGame', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '1__name',self._waldo_classes["WaldoTextVariable"](  # the type of waldo variable to create
                '1__name', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '2__pos',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '2__pos', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '3__initialized',self._waldo_classes["WaldoTrueFalseVariable"](  # the type of waldo variable to create
                '3__initialized', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(False ,_active_event)
            ))

            self._global_var_store.add_var(
                '4__getMSG',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '4__getMSG', # variable's name
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
                _to_return = self._onCreate(_root_event,_ctx ,init_get_MSG,n,[])
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

        def _onCreate(self,_active_event,_context,init_get_MSG,n,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                init_get_MSG = _context.func_turn_into_waldo_var(init_get_MSG,True,_active_event,self._host_uuid,False,[],False)
                n = _context.turn_into_waldo_var_if_was_var(n,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                init_get_MSG = _context.func_turn_into_waldo_var(init_get_MSG,True,_active_event,self._host_uuid,False,[],False)
                n = _context.turn_into_waldo_var_if_was_var(n,True,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = init_get_MSG
            if not _context.assign(_context.global_store.get_var_if_exists("4__getMSG"),_tmp0,_active_event):
                pass

            _tmp0 = n
            if not _context.assign(_context.global_store.get_var_if_exists("1__name"),_tmp0,_active_event):
                pass

            _tmp0 = -1 
            if not _context.assign(_context.global_store.get_var_if_exists("0__currGame"),_tmp0,_active_event):
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
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__send_msg(self,_active_event,_context,msg,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False,False)

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__SeqSendMSG(_active_event,_context,msg,) if _context.set_msg_send_initialized_bit_false() else None)


        def send_cmd(self,cmd,toEnter):

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
                _to_return = self._endpoint_func_call_prefix__waldo__send_cmd(_root_event,_ctx ,cmd,toEnter,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__send_cmd(self,_active_event,_context,cmd,toEnter,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                cmd = _context.turn_into_waldo_var_if_was_var(cmd,True,_active_event,self._host_uuid,False,False)
                toEnter = _context.turn_into_waldo_var_if_was_var(toEnter,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                cmd = _context.turn_into_waldo_var_if_was_var(cmd,True,_active_event,self._host_uuid,False,False)
                toEnter = _context.turn_into_waldo_var_if_was_var(toEnter,True,_active_event,self._host_uuid,False,False)

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple((self._partner_endpoint_msg_func_call_prefix__waldo__SeqSendCMD(_active_event,_context,cmd,toEnter,) if _context.set_msg_send_initialized_bit_false() else None) if 0 in _returning_to_public_ext_array else _context.de_waldoify((self._partner_endpoint_msg_func_call_prefix__waldo__SeqSendCMD(_active_event,_context,cmd,toEnter,) if _context.set_msg_send_initialized_bit_false() else None),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple((self._partner_endpoint_msg_func_call_prefix__waldo__SeqSendCMD(_active_event,_context,cmd,toEnter,) if _context.set_msg_send_initialized_bit_false() else None))




        def getName(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__getName(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__getName(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__name") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("1__name"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("1__name"))




        def getGame(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__getGame(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__getGame(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("0__currGame") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("0__currGame"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("0__currGame"))




        def setGame(self,n):

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
                _to_return = self._endpoint_func_call_prefix__waldo__setGame(_root_event,_ctx ,n,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__setGame(self,_active_event,_context,n,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                n = _context.turn_into_waldo_var_if_was_var(n,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                n = _context.turn_into_waldo_var_if_was_var(n,True,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = n
            if not _context.assign(_context.global_store.get_var_if_exists("0__currGame"),_tmp0,_active_event):
                pass



        def retrieveMSG(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__retrieveMSG(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__retrieveMSG(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass

            (self._partner_endpoint_msg_func_call_prefix__waldo__SeqRetrieveMSG(_active_event,_context,) if _context.set_msg_send_initialized_bit_false() else None)

        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__SeqSendMSG(self,_active_event,_context,msg=None,_returning_to_public_ext_array=None):

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
                        "29__msg", _context.convert_for_seq_local(msg,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "29__msg", _context.convert_for_seq_local(msg,_active_event,self._host_uuid)
                    )

                    pass


                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'receiveMSG',_threadsafe_queue, '_first_msg')
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

        def _partner_endpoint_msg_func_call_prefix__waldo__SeqSendCMD(self,_active_event,_context,command=None,toEnterVote=None,_returning_to_public_ext_array=None):

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
                        "35__command", _context.convert_for_seq_local(command,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "36__toEnterVote", _context.convert_for_seq_local(toEnterVote,_active_event,self._host_uuid)
                    )

                    pass

                else:

                    _context.sequence_local_store.add_var(
                        "35__command", _context.convert_for_seq_local(command,_active_event,self._host_uuid)
                    )

                    _context.sequence_local_store.add_var(
                        "36__toEnterVote", _context.convert_for_seq_local(toEnterVote,_active_event,self._host_uuid)
                    )

                    pass

                numPlayers = 0
                _context.sequence_local_store.add_var(
                    "31__numPlayers",_context.convert_for_seq_local(numPlayers,_active_event,self._host_uuid))
                temp = self._waldo_classes["WaldoSingleThreadListVariable"](  # the type of waldo variable to create
                    '32__temp', # variable's name
                    self._host_uuid, # host uuid var name
                    False,  # if peered, True, otherwise, False
                    
                )
                _context.sequence_local_store.add_var(
                    "32__temp",_context.convert_for_seq_local(temp,_active_event,self._host_uuid))
                theGame = _context.get_val_if_waldo(-1 ,_active_event)
                _context.sequence_local_store.add_var(
                    "33__theGame",_context.convert_for_seq_local(theGame,_active_event,self._host_uuid))
                players = 0
                _context.sequence_local_store.add_var(
                    "37__players",_context.convert_for_seq_local(players,_active_event,self._host_uuid))

                pass

            _tmp0 = _context.global_store.get_var_if_exists("0__currGame")
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("33__theGame"),_tmp0,_active_event):
                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'receiveCMD',_threadsafe_queue, '_first_msg')
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


            return _context.sequence_local_store.get_var_if_exists("37__players")

        def _partner_endpoint_msg_func_call_prefix__waldo__SeqRetrieveMSG(self,_active_event,_context,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    pass

                else:

                    pass

                position = 0
                _context.sequence_local_store.add_var(
                    "41__position",_context.convert_for_seq_local(position,_active_event,self._host_uuid))
                t = ""
                _context.sequence_local_store.add_var(
                    "42__t",_context.convert_for_seq_local(t,_active_event,self._host_uuid))
                shift = _context.get_val_if_waldo(False ,_active_event)
                _context.sequence_local_store.add_var(
                    "43__shift",_context.convert_for_seq_local(shift,_active_event,self._host_uuid))
                hasInitialized = False
                _context.sequence_local_store.add_var(
                    "44__hasInitialized",_context.convert_for_seq_local(hasInitialized,_active_event,self._host_uuid))

                pass

            _tmp0 = _context.global_store.get_var_if_exists("2__pos")
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("41__position"),_tmp0,_active_event):
                pass

            _tmp0 = _context.global_store.get_var_if_exists("3__initialized")
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("44__hasInitialized"),_tmp0,_active_event):
                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'obtainMSG',_threadsafe_queue, '_first_msg')
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

        def _partner_endpoint_msg_func_call_prefix__waldo__SeqCurrGame(self,_active_event,_context,_returning_to_public_ext_array=None):

            _first_msg = False
            if not _context.set_msg_send_initialized_bit_true():
                # we must load all arguments into sequence local data and perform
                # initialization on sequence local data....start by loading
                # arguments into sequence local data
                # below tells the message send that it must serialize and
                # send all sequence local data.
                _first_msg = True
                if _context.check_and_set_from_endpoint_call_false():

                    pass

                else:

                    pass

                currPos = 0
                _context.sequence_local_store.add_var(
                    "47__currPos",_context.convert_for_seq_local(currPos,_active_event,self._host_uuid))

                pass



            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,'obtainGame',_threadsafe_queue, '_first_msg')
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

        def _partner_endpoint_msg_func_call_prefix__waldo__update(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = _context.sequence_local_store.get_var_if_exists("31__numPlayers")
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("37__players"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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


        def _partner_endpoint_msg_func_call_prefix__waldo__put(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = _context.sequence_local_store.get_var_if_exists("44__hasInitialized")
            if not _context.assign(_context.global_store.get_var_if_exists("3__initialized"),_tmp0,_active_event):
                pass

            _tmp0 = _context.sequence_local_store.get_var_if_exists("41__position")
            if not _context.assign(_context.global_store.get_var_if_exists("2__pos"),_tmp0,_active_event):
                pass

            if _context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("43__shift"),_active_event):
                _tmp0 = (_context.get_val_if_waldo(_context.global_store.get_var_if_exists("2__pos"),_active_event) + _context.get_val_if_waldo(1 ,_active_event))
                if not _context.assign(_context.global_store.get_var_if_exists("2__pos"),_tmp0,_active_event):
                    pass


                pass


            if _context.get_val_if_waldo((_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("42__t"),_active_event) != _context.get_val_if_waldo('' ,_active_event)),_active_event):
                _context.signal_call(_active_event,_context.global_store.get_var_if_exists("4__getMSG"),_context.sequence_local_store.get_var_if_exists("42__t"),)


                pass





            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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


        def _partner_endpoint_msg_func_call_prefix__waldo__receiveGame(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = _context.sequence_local_store.get_var_if_exists("47__currPos")
            if not _context.assign(_context.global_store.get_var_if_exists("2__pos"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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
        def __init__(self,_waldo_classes,_host_uuid,_conn_obj,init_display_msg_func,init_vote_func):

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
                '17__gameStatus',self._waldo_classes["WaldoListVariable"](  # the type of waldo variable to create
                '17__gameStatus', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '18__msgs',self._waldo_classes["WaldoListVariable"](  # the type of waldo variable to create
                '18__msgs', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ))

            self._global_var_store.add_var(
                '19__msgsLength',self._waldo_classes["WaldoNumVariable"](  # the type of waldo variable to create
                '19__msgsLength', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                _context.get_val_if_waldo(-1 ,_active_event)
            ))

            self._global_var_store.add_var(
                '20__display_msg_func',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '20__display_msg_func', # variable's name
                _host_uuid, # host uuid var name
                False,  # if peered, True, otherwise, False
                
            ).set_external_args_array([]))

            self._global_var_store.add_var(
                '21__vote_func',self._waldo_classes["WaldoFunctionVariable"](  # the type of waldo variable to create
                '21__vote_func', # variable's name
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
                _to_return = self._onCreate(_root_event,_ctx ,init_display_msg_func,init_vote_func,[])
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

        def _onCreate(self,_active_event,_context,init_display_msg_func,init_vote_func,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[],False)
                init_vote_func = _context.func_turn_into_waldo_var(init_vote_func,True,_active_event,self._host_uuid,False,[],False)

                pass

            else:
                init_display_msg_func = _context.func_turn_into_waldo_var(init_display_msg_func,True,_active_event,self._host_uuid,False,[],False)
                init_vote_func = _context.func_turn_into_waldo_var(init_vote_func,True,_active_event,self._host_uuid,False,[],False)

                pass

            _tmp0 = init_display_msg_func
            if not _context.assign(_context.global_store.get_var_if_exists("20__display_msg_func"),_tmp0,_active_event):
                pass

            _tmp0 = init_vote_func
            if not _context.assign(_context.global_store.get_var_if_exists("21__vote_func"),_tmp0,_active_event):
                pass

        ### USER DEFINED METHODS ###

        def receiveStatus(self,status):

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
                _to_return = self._endpoint_func_call_prefix__waldo__receiveStatus(_root_event,_ctx ,status,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__receiveStatus(self,_active_event,_context,status,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                status = _context.turn_into_waldo_var_if_was_var(status,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                status = _context.turn_into_waldo_var_if_was_var(status,False,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = self._waldo_classes["WaldoSingleThreadListVariable"]("garbage_name",
                self._host_uuid,
                False,
                [])
            if not _context.assign(_context.global_store.get_var_if_exists("17__gameStatus"),_tmp0,_active_event):
                pass

            num = 0
            for _secret_waldo_for_iter____num in _context.get_for_iter(status,_active_event):
                num = _context.write_val(num,_secret_waldo_for_iter____num,_active_event)
                _context.global_store.get_var_if_exists("17__gameStatus").get_val(_active_event).append_val(_active_event,_context.get_val_if_waldo(num,_active_event))

                pass



        def addMSG(self,msg):

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
                _to_return = self._endpoint_func_call_prefix__waldo__addMSG(_root_event,_ctx ,msg,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__addMSG(self,_active_event,_context,msg,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                msg = _context.turn_into_waldo_var_if_was_var(msg,True,_active_event,self._host_uuid,False,False)

                pass

            if _context.get_val_if_waldo((_context.get_val_if_waldo(msg,_active_event) != _context.get_val_if_waldo('' ,_active_event)),_active_event):
                _context.global_store.get_var_if_exists("18__msgs").get_val(_active_event).append_val(_active_event,_context.get_val_if_waldo(msg,_active_event))

                pass




        def getMSGS(self):

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
                _to_return = self._endpoint_func_call_prefix__waldo__getMSGS(_root_event,_ctx ,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__getMSGS(self,_active_event,_context,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():

                pass

            else:

                pass


            if _returning_to_public_ext_array != None:
                # must de-waldo-ify objects before passing back
                return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("18__msgs") if 0 in _returning_to_public_ext_array else _context.de_waldoify(_context.global_store.get_var_if_exists("18__msgs"),_active_event))


            # otherwise, use regular return mechanism... do not de-waldo-ify
            return _context.flatten_into_single_return_tuple(_context.global_store.get_var_if_exists("18__msgs"))




        def changeMSGS(self,list):

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
                _to_return = self._endpoint_func_call_prefix__waldo__changeMSGS(_root_event,_ctx ,list,[])
                # try committing root event
                _root_event.request_commit()
                _commit_resp = _root_event.event_complete_queue.get()
                if isinstance(_commit_resp,self._waldo_classes["CompleteRootCallResult"]):
                    # means it isn't a backout message: we're done
                    return _to_return
                elif isinstance(_commit_resp,self._waldo_classes["StopRootCallResult"]):
                    raise self._waldo_classes["StoppedException"]()



        def _endpoint_func_call_prefix__waldo__changeMSGS(self,_active_event,_context,list,_returning_to_public_ext_array=None):
            if _context.check_and_set_from_endpoint_call_false():
                list = _context.turn_into_waldo_var_if_was_var(list,True,_active_event,self._host_uuid,False,False)

                pass

            else:
                list = _context.turn_into_waldo_var_if_was_var(list,False,_active_event,self._host_uuid,False,False)

                pass

            _tmp0 = list
            if not _context.assign(_context.global_store.get_var_if_exists("18__msgs"),_tmp0,_active_event):
                pass

            _tmp0 = _context.handle_len(_context.global_store.get_var_if_exists("18__msgs"),_active_event)
            if not _context.assign(_context.global_store.get_var_if_exists("19__msgsLength"),_tmp0,_active_event):
                pass


        ### USER DEFINED SEQUENCE BLOCKS ###

        ### User-defined message send blocks ###

        ### User-defined message receive blocks ###

        def _partner_endpoint_msg_func_call_prefix__waldo__receiveMSG(self,_active_event,_context,_returning_to_public_ext_array=None):

            _context.signal_call(_active_event,_context.global_store.get_var_if_exists("20__display_msg_func"),_context.sequence_local_store.get_var_if_exists("29__msg"),)




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,None,_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if None != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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


        def _partner_endpoint_msg_func_call_prefix__waldo__receiveCMD(self,_active_event,_context,_returning_to_public_ext_array=None):

            if _context.get_val_if_waldo((_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("35__command"),_active_event) > _context.get_val_if_waldo(-3 ,_active_event)),_active_event):
                _context.signal_call(_active_event,_context.global_store.get_var_if_exists("21__vote_func"),_context.sequence_local_store.get_var_if_exists("35__command"),_context.sequence_local_store.get_var_if_exists("36__toEnterVote"),)


                pass


            n = 0
            for _secret_waldo_for_iter____n in _context.get_for_iter(_context.global_store.get_var_if_exists("17__gameStatus"),_active_event):
                n = _context.write_val(n,_secret_waldo_for_iter____n,_active_event)
                _context.sequence_local_store.get_var_if_exists("32__temp").get_val(_active_event).append_val(_active_event,_context.get_val_if_waldo(n,_active_event))

                pass

            if _context.get_val_if_waldo((_context.get_val_if_waldo(_context.handle_len(_context.sequence_local_store.get_var_if_exists("32__temp"),_active_event),_active_event) >= _context.get_val_if_waldo(3 ,_active_event)),_active_event):
                if _context.get_val_if_waldo((_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("32__temp").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("33__theGame"),_active_event)),_active_event) >= _context.get_val_if_waldo(1 ,_active_event)),_active_event):
                    _tmp0 = _context.sequence_local_store.get_var_if_exists("32__temp").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("33__theGame"),_active_event))
                    if not _context.assign(_context.sequence_local_store.get_var_if_exists("31__numPlayers"),_tmp0,_active_event):
                        pass


                    pass



                pass





            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__update",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__update" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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


        def _partner_endpoint_msg_func_call_prefix__waldo__obtainMSG(self,_active_event,_context,_returning_to_public_ext_array=None):

            if _context.get_val_if_waldo((_context.get_val_if_waldo((_context.get_val_if_waldo(_context.global_store.get_var_if_exists("19__msgsLength"),_active_event) >= _context.get_val_if_waldo(0 ,_active_event)),_active_event) and _context.get_val_if_waldo(( not ( _context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("44__hasInitialized"),_active_event) )),_active_event)),_active_event):
                _tmp0 = (_context.get_val_if_waldo(_context.handle_len(_context.global_store.get_var_if_exists("18__msgs"),_active_event),_active_event) - _context.get_val_if_waldo(1 ,_active_event))
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("41__position"),_tmp0,_active_event):
                    pass

                _tmp0 = True 
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("44__hasInitialized"),_tmp0,_active_event):
                    pass


                pass


            if _context.get_val_if_waldo((_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("41__position"),_active_event) < _context.get_val_if_waldo(_context.handle_len(_context.global_store.get_var_if_exists("18__msgs"),_active_event),_active_event)),_active_event):
                _tmp0 = _context.global_store.get_var_if_exists("18__msgs").get_val(_active_event).get_val_on_key(_active_event,_context.get_val_if_waldo(_context.sequence_local_store.get_var_if_exists("41__position"),_active_event))
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("42__t"),_tmp0,_active_event):
                    pass

                _tmp0 = True 
                if not _context.assign(_context.sequence_local_store.get_var_if_exists("43__shift"),_tmp0,_active_event):
                    pass


                pass





            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__put",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__put" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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


        def _partner_endpoint_msg_func_call_prefix__waldo__obtainGame(self,_active_event,_context,_returning_to_public_ext_array=None):

            _tmp0 = _context.handle_len(_context.global_store.get_var_if_exists("18__msgs"),_active_event)
            if not _context.assign(_context.sequence_local_store.get_var_if_exists("47__currPos"),_tmp0,_active_event):
                pass




            _threadsafe_queue = self._waldo_classes["Queue"].Queue()
            _active_event.issue_partner_sequence_block_call(
                _context,"_partner_endpoint_msg_func_call_prefix__waldo__receiveGame",_threadsafe_queue,False)
            # must wait on the result of the call before returning

            if "_partner_endpoint_msg_func_call_prefix__waldo__receiveGame" != None:
                # means that we have another sequence item to execute next

                _queue_elem = _threadsafe_queue.get()




                if isinstance(_queue_elem,self._waldo_classes["BackoutBeforeReceiveMessageResult"]):
                    # back everything out: 
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

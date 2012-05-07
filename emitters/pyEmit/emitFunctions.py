#!/usr/bin/python

import emitHelper;


class Function(object):
    def __init__(self,name,astNode,protObj,declArgListIndex):
        '''
        @param {String} name -- Should already be guaranteed not to
        collide with python variable and other global vars.
        
        @param {Int} declArgListIndex -- Each function astNode
        (public, msgReceive, ...) has many children.  declArgListIndex is
        the index of astNode.children that contains declArgList appears.
        '''
        self.name = name;
        self.astNode = astNode;
        self.protObj = protObj;
        self.endpoint = self.protObj.currentEndpoint;
        self.declArgListIndex = declArgListIndex;
        
    def emit():
        errMsg = '\nBehram error: pure virtual method emit of Function ';
        errMsg += 'called.\n';
        assert(False);

    def pythonizeName(self):
        return self.name;
        
    def createMethodHeader(self):
        #already know that self.name does not conflict with python
        #because was checked before constructed.
        methodHeader = 'def %s(self' % self.name;

        
        #fill in arguments
        declArgsList = self.astNode.children[self.declArgListIndex];
        for s in declArgsList.children:
            #each s is a declArg
            if (len(s.children) == 0):
                continue;


            argName = s.children[1].value;
            argName = self.endpoint.varName(argName);
            methodHeader += ', ' + argName;
        
        methodHeader += '):\n';
        return methodHeader;


class InternalFunction(Function):
    def __init__(self,name,astNode,protObj):
        #see astBuilder or the graphical ast:
        functionArgDeclIndex = 2;        
        super(InternalFunction,self).__init__(name,astNode,protObj,functionArgDeclIndex);
    def emit(self):
        print('\nBehram error: in InternalFunction, need to finish emit method\n');
        methodHeader = self.createMethodHeader();
        methodBody = 'pass';
        
        returnString = emitHelper.indentString(methodHeader,1);
        returnString += emitHelper.indentString(methodBody,2);
        return returnString;


class PublicFunction(Function):
    def __init__(self,name,astNode,protObj):
        #see astBuilder or the graphical ast:
        functionArgDeclIndex = 2;
        super(PublicFunction,self).__init__(name,astNode,protObj,functionArgDeclIndex);

    def emit(self):
        print('\nBehram error: in PublicFunction, need to finish emit method\n');
        methodHeader = self.createMethodHeader();        

        methodBody = 'pass;';
        
        returnString = emitHelper.indentString(methodHeader,1);
        returnString += emitHelper.indentString(methodBody,2);
        return returnString;

class MsgFunction(Function):
    def __init__ (self,name,protObj):
        #see astBuilder or the graphical ast:
        functionArgDeclIndex = 1;
        self.sendsTo = None;
        
        super(MsgFunction,self).__init__(name,None,protObj,functionArgDeclIndex);

        
    def setSendsTo(self,sendsTo):
        '''
        Each message function should know the function on the other
        endpoint it is sending to.  This allows it to specify which
        handler on the receiver should fire in the message.
        '''
        self.sendsTo = sendsTo;


    def setAstNode(self,astNode):
        '''
        Message functions are created when running through the traces
        section of the code (so that it's easy to determine which msg
        function sends a msg to which other msg function).  At that
        point, we do not have the ast node corresponding to the actual
        message function.  Therefore, we have to allow ourselves to
        set it separately and later.
        '''
        self.astNode = astNode;

        # FIXME: super-hack.
        # lkjs
        self.endpoint = self.protObj.currentEndpoint;


    def caseBasedDispatch(self,first,indentLevel):
        '''
        Each message should be structured to include the name of the
        function on the other endpoint that should handle it.  The
        code that handles the message labeling itself is a large
        if-elif-else statement found in the _sendMsg function of the
        emitted code (and populated in the @see
        emitGeneralSendMessageUtility function of class Endpoint in
        emitEndpoint.py).  In general, it should end up looking
        something like:

        dispatchTo = None;
        if (funcNameFrom == '_msgRecvTwo'):
            dispatchTo = '_msgRecvThree';
        elif(funcNameFrom == '_msgRecvFour'):
            dispatchTo = STREAM_TAIL_SENTINEL;
        else:
            errMsg = '\nBehram Error.  Provided an invalid ';
            errMsg += 'funcNameFrom argument in Pong.\n';
            print(errMsg);
            assert(False);
            
        Each if/elif statement itself is composed by a separate
        MsgFunction in this method.
        '''

        ifElifOperator = 'elif';
        if (first):
            ifElifOperator = 'if';

        ifHead = ifElifOperator + " (funcNameFrom == '" + self.pythonizeName() + "'):\n";

        ifBody = "dispatchTo  = ";

        if (self.sendsTo == None):
            # means that this was the last message receive in a trace
            # line: we should set dispacthTo equal to the sentinnel
            # value representing this case.
            ifBody += 'STREAM_TAIL_SENTINEL;\n';
        else:
            ifBody += "'" + self.sendsTo.pythonizeName() + "';\n";

            
        indentedHead = emitHelper.indentString(ifHead,indentLevel);
        indentedBody = emitHelper.indentString(ifBody,indentLevel+1);

        return indentedHead + indentedBody;
        
        
class MsgSendFunction(MsgFunction):
    def __init__(self,name,protObj):
        super(MsgSendFunction,self).__init__(name,protObj);

    def pythonizeName(self):
        '''
        Using a convention of changing a msg send function's name from
        <FuncName> to _msgSend<FuncName>
        '''
        return '_msgSend' + self.name;

        
    def emit(self):
        print('\nBehram error: in MsgSendFunction, need to finish emit method\n');

        methodHeader = self.createMethodHeader();
        
        funcBodyNode = self.astNode.children[2];
        methodBody = emitHelper.runFunctionBodyInternalEmit(funcBodyNode,self.protObj,self.endpoint);
        
        returnString = emitHelper.indentString(methodHeader,1);
        returnString += emitHelper.indentString(methodBody,2);
        return returnString;


        
class MsgReceiveFunction(MsgFunction):
    def __init__(self,name,protObj):
        super(MsgReceiveFunction,self).__init__(name,protObj);

    def pythonizeName(self):
        '''
        Using a convention of changing a msg send function's name from
        <FuncName> to _msgRecv<FuncName>
        '''
        return '_msgRecv' + self.name;
        
        
    def emit(self):
        print('\nBehram error: in MsgReceiveFunction, need to finish emit method\n');
        methodHeader = self.createMethodHeader();                
        methodBody = 'pass;';
        
        returnString = emitHelper.indentString(methodHeader,1);
        returnString += emitHelper.indentString(methodBody,2);
        return returnString;

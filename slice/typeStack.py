#!/usr/bin/env python
import util;

class TypeStack(object):
    IDENTIFIER_TYPE_SHARED = 0;
    IDENTIFIER_TYPE_ENDPOINT_GLOBAL = 1;
    IDENTIFIER_TYPE_MSG_SEQ_GLOBAL = 2;
    IDENTIFIER_TYPE_FUNCTION_ARGUMENT = 3;
    IDENTIFIER_TYPE_LOCAL = 4;
    IDENTIFIER_TYPE_FUNCTION_CALL = 5;
    IDENTIFIER_TYPE_RETURN_STATEMENT = 6;

    def __init__(self,prevStack=None):
        self.stack  = []; #last element in array is always top of stack.
        self.endNames = {};
        self.mEndpointName = None;
        
        if prevStack != None:
            for ctx in prevStack.stack:
                self.stack.append(ctx);

            self.endNames = prevStack.endNames;

    def addMyEndpointName(self,endName):
        self.mEndpointName = endName;
        self._addEndpointName(endName);

    def addOtherEndpointName(self,endName):
        self._addEndpointName(endName);
    
    def _addEndpointName(self,endName):
        self.endNames[endName] = True;
        
    def isEndpointName (self,toTest):
        val = self.endNames.get(toTest,None);
        if val == None:
            return False;
        return True;

    def hashFuncName(self,funcName):
        '''
        @param {String} funcName
        '''
        if self.mEndpointName == None:
            errMsg = '\nBehram error: cannot hash function name ';
            errMsg += 'without and endpoint name.\n';
            print(errMsg);
            assert(False);
        return self.mEndpointName + '_-_-_' + funcName;

    
    def getLabelAs(self):
        topStack = self.checkStackLen('changeLabelAs');
        return topStack.labelAs;
    
    def changeLabelAs(self,newLabelAs):
        topStack = self.checkStackLen('changeLabelAs');
        topStack.labelAs = newLabelAs;
        
    def pushContext(self,labelAs,currentFunctionDep):
        self.stack.append(Context(labelAs,currentFunctionDep));

    def popContext(self):
        self.checkStackLen('popContext');
        self.stack.pop();

    def addIdentifier(
        self,identifierName,isMutable,identifierType=None,
        argPosition=None):
        '''
        @see Context.addIdentifier
        '''
        topStack = self.checkStackLen('addIdentifier');        
        return topStack.addIdentifier(
            identifierName,isMutable,identifierType,argPosition);

    def addIdentifierAsNtt(self,ntt):
        topStack = self.checkStackLen('addIdentifierAsNtt');
        return topStack.addIdentifierAsNtt(ntt);

    

    def getIdentifier(self,identifierName):
        topStack = self.checkStackLen('getIdentifier');

        backwardsRange = range(0,len(self.stack));
        backwardsRange.reverse();
        for contextIndex in backwardsRange:
            context = self.stack[contextIndex];
            exists  = context.getIdentifier(identifierName);
            if exists != None:
                return exists;

        errMsg = '\nBehram error: all identifiers should be defined by now.  ';
        errMsg += 'But "' + identifierName + '" was not.\n';
        print(errMsg);
        assert(False);


    def addToVarReadSet(self,ntt):
        '''
        If we are inside a function, ensure that that function is
        labeled to know that variable with nodeName is a variable
        inside of it.  ntt is NameTypeTuple, which has information on
        the name of the variable, its type, and whether it's mutable
        or not.
        '''
        topStack = self.checkStackLen('addToVarReadSet');                
        curFuncDep = topStack.currentFunctionDep;
        if curFuncDep != None:
            # happened inside a function instead of happening
            # inside of an endpoint global section.
            curFuncDep.addToVarReadSet(ntt);

    def addReadsToVarReadSet(self,ntt,reads):
        '''
        ntt is the node that we are adding the reads for.  Ie, ntt is
        being written to, and its writes at least partially depend on
        the ntt-s in the array reads.
        
        If we are inside of a function, then tell the function that
        variable with ntt ntt relies on reads and writes from
        the NodeNameTuples populating the arrays reads and writes.
        '''
        topStack = self.checkStackLen('addReadsWritesToVarReadSet');
        curFuncDep = topStack.currentFunctionDep;
        if curFuncDep != None:
            # happened inside a function instead of happening
            # inside of an endpoint global section.
            curFuncDep.addReadsToVarReadSet(ntt,reads);

    def addRead(self,ntt):
        '''
        If we are inside of a function, then tell the function that
        the function relies on the attached ntt.
        '''
        topStack = self.checkStackLen('addReadsWritesToVarReadSet');
        topStack.addRead(ntt);
            
    def addFuncCall(self,nameOfFunc,funcArgReads):
        '''
        @see FuncCallNtt for description of arguments.

        Called whenever code in Waldo function calls another function.
        '''
        topStack = self.checkStackLen('addFuncCall');
        return topStack.addFuncCall(nameOfFunc,funcArgReads);

    def addReturnStatement(self,returnReads):
        '''
        @see ReturnStatementNtt
        
        Called whenever code in source has a return statement.
        '''
        topStack = self.checkStackLen('addReturnStatement');
        return topStack.addReturnStatement(returnReads);
        
    
    def getReadIndex(self):
        '''
        @see getReadIndex of Context
        '''
        stackTop = self.checkStackLen('getReadIndex');
        return stackTop.getReadIndex();

    def getReadsAfter(self,afterPoint):
        '''
        @see getReadIndex of Context
        '''
        stackTop = self.checkStackLen('getReadsAfter');
        return stackTop.getReadsAfter(afterPoint);
    

    def checkStackLen(self,operatioName):
        if len(self.stack) <= 0:
            errMsg = '\nBehram error.  Stack underflow when trying ';
            errMsg += 'to perform operation ' + operationName + '.\n';
            print(errMsg);
            assert(False);
        return self.stack[-1];
    
    

class Context(object):
    def __init__(self,labelAs,currentFunctionDep):
        '''
        currentFunctionDep can be None if getting shared or globals.
        '''
        # dict from identifier name to NameTypeTuple-s, these contain
        # only local variables and arguments passed into function
        self.dict = {};

        # also contains func calls.
        self.reads = [];
        self.labelAs = labelAs;
        self.currentFunctionDep = currentFunctionDep;


    def addFuncCall(self,nameOfFunc,funcArgReads):
        '''
        @see FuncCallNtt for description of arguments.
        
        Currently, treat ntt associated with func call the same way we
        treat an ntt associated with a read.
                
        @returns {FuncCallNtt} 
        '''
        ntt = FuncCallNtt(nameOfFunc,funcArgReads);
        self.reads.append(ntt);

        if self.currentFunctionDep != None:
            # happened inside a function instead of happening
            # inside of an endpoint global section.
            self.currentFunctionDep.addFuncCall(ntt);

    def addReturnStatement(self,returnReads):
        '''
        @see ReturnStatement ntt for description of arguments.

        @returns {ReturnStatementNtt}
        '''
        ntt = ReturnStatementNtt(returnReads);
        self.reads.append(ntt);
        if self.currentFunctionDep != None:
            self.currentFunctionDep.addReturnStatement(ntt);
        else:
            errMsg = '\nBehram error.  Should never get return ';
            errMsg += 'statement outside of a function definition.\n';
            print(errMsg);
            assert(False);
            
        
    def getReadIndex(self):
        '''
        want to support the semantics: 'get all reads after some
        point'.  This let's us name that starting point.  Then, can
        call getReadsAfter to get all reads that happened between now
        and when getReadIndex was called.
        '''
        return len(self.reads);

    def getReadsAfter(self,afterPoint):
        '''
        @see getReadIndex
        '''
        return self.reads[afterPoint:];

        
    def addRead(self,ntt):
        '''
        @param {NameTypeTuple} ntt.
        '''
        self.reads.append(ntt);

        if self.currentFunctionDep != None:
            # happened inside a function instead of happening
            # inside of an endpoint global section.
            self.currentFunctionDep.addFuncReads([ntt]);
        
    def getIdentifier(self,identifierName):
        '''
        @returns None if identifierName does not exist in this context
                 NameTypeTuple otherwise
        '''
        val = self.dict.get(identifierName,None);
        return val;
        
    def addIdentifier(
        self,identifierName,isMutable,identifierType,argPosition):
        '''
        @param {String} identifierName
        
        @param {Int} One of TypeStack.IDENTIFIER_TYPE*-s Indicates
        what type of variable this is in the local context.  None if
        just supposed to use the label that is being saved in labelAs.

        @param {Int or None} argPosition --- If identifierType is
        TypeStack.IDENTIFIER_TYPE_FUNCTION_ARGUMENT, then also save
        the argument's position in the name type tuple.  Otherwise,
        save None
        '''
        if identifierType == None:
            identifierType = self.labelAs;
        ntt = NameTypeTuple(identifierName,identifierType,isMutable,argPosition);
        self.dict[identifierName] = ntt;
        return ntt;

    def addIdentifierAsNtt(self,ntt):
        self.dict[identifierName] = ntt;
        return ntt;
    
    
class NameTypeTuple(object):
    staticId = 0;
    def __init__(self,varName,varType,isMutable,argPosition):
        '''
        @param {String} varName
        @param {Int} varType --- TypeStack.IDENTIFIER_TYPE_*;
        
        @param {Bool} isMutable --- True if variable is a list or map,
        false otherwise.

        @param {Int or None} argPosition --- If (and only if) this is
        a IDENTIFIER_TYPE_FUNCTION_ARGUMENT, then this will be an
        integer representing the zero-indexed position of the argument
        passed to the function.  Otherwise, it must be None.
        '''
        self.varName = varName;
        self.varType = varType;
        self.mutable = isMutable;
        self._mark = False;

        self.id = NameTypeTuple.staticId;
        NameTypeTuple.staticId += 1;
        
        if ((argPosition != None) and
            (varType != TypeStack.IDENTIFIER_TYPE_FUNCTION_ARGUMENT)):
            errMsg = '\nBehram error: should not receive an arg position ';
            errMsg += 'with a variable that is not a function argument.\n';
            print(errMsg);
            assert(False);

        self.argPosition = argPosition;

    def jsonize(self):
        returner = {};
        returner['id'] = self.id;
        returner['varName'] = self.varName;
        returner['varType'] = self.varType;
        returner['mutable'] = 1 if self.mutable else 0;
        returner['argPosition'] = -1 if self.argPosition == None else self.argPosition;
        
        return util.toJsonPretty(returner);

        
    def mark(self):
        self._mark = True;
    def unmark(self):
        self._mark = False;
    def isMarked(self):
        return self._mark;

    def replaceFuncArguments(self,foundArgsDict):
        '''
        @see _changeArgIds in FunctionDeps
        '''
        return;
    



    
class ReturnStatementNtt(NameTypeTuple):
    def __init__(self,returnStatementReads):
        '''
        @param {Array} returnStatementReads --- each element is a
        NameTypeTuple.

        Corresponds to a return statement that 
        '''
        NamTypeTuple.__init__(
            self,'return statement',
            TypeStack.IDENTIFIER_TYPE_RETURN_STATEMENT,False,None);

        self.returnStatementReads = returnStatementReads;

    def replaceFuncArguments(self,foundArgsDict):
        '''
        @see _changeArgIds in FunctionDeps

        Needs to go through its entire read set and replace any
        function arguments with those in foundArgsDict.
        '''
        for readNttIndex in range(0,len(self.returnStatementReads)):
            readNtt = self.returnStatementReads[readNttIndex];
            
            if readNtt.id in foundArgsDict:
                self.returnStatementReads[readNttIndex] = foundArgsDict[readNtt.id];
            else:
                readNtt.replaceFuncArguments(foundArgsDict);

        

class FuncCallNtt(NameTypeTuple):

    def __init__(self,nameOfFunc,funcArgReads):
        '''
        @param {String} nameOfFunc --- the name of a function that
        is being called.

        @param {Array of arrays} funcArgReads --- Each element of the
        array is an array that corresponds to the reads of the
        corresponding positional argument passed to the function call.
        For example, if funcArgReads is [a,b,c].  Then a is an array
        of NameTypeTuples that correspond to the reads made to provide
        this positional argument.
        '''
        NameTypeTuple.__init__(
            self,nameOfFunc,TypeStack.IDENTIFIER_TYPE_FUNCTION_CALL,False,None);
        
        self.funcArgReads = funcArgReads;

    def hashSignature(self):
        '''
        @returns {String} --- generates a signature of this function
        call.  Only function calls to the same functions whose
        arguments have the read set should have the same signature.
        If two have the same signature, that means that the
        global/shared write and read sets of one will be the same as
        the global/shared write and read sets of the other.
        '''
        returner = str(self.varName) + '|_*_| ';
        for positionArgReads in self.funcArgReads:

            for readNtt in positionArgReads:
                if readNtt.varType == TypeStack.IDENTIFIER_TYPE_FUNCTION_CALL:
                    returner += readNtt.hashSignature();
                else:
                    returner += str(readNtt.id);
                returner += '-^-';

            
            returner += '&%&';
        
        return returner;


    def replaceFuncArguments(self,foundArgsDict):
        '''
        @see _changeArgIds in FunctionDeps

        Needs to go through its entire read set and replace any
        function arguments with those in foundArgsDict.
        '''
        for argArray in self.funcArgReads:

            for readIndex in range(0,len(argArray)):
                readNtt = argArray[readIndex];

                if readNtt.id in foundArgsDict:
                    argArray[readIndex] = foundArgsDict[readNtt.id];
                else:
                    readNtt.replaceFuncArguments(foundArgsDict);
    

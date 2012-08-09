#!/usr/bin/env python


class TypeStack(object):
    IDENTIFIER_TYPE_SHARED = 0;
    IDENTIFIER_TYPE_ENDPOINT_GLOBAL = 1;
    IDENTIFIER_TYPE_MSG_SEQ_GLOBAL = 2;
    IDENTIFIER_TYPE_FUNCTION_ARGUMENT = 3;
    IDENTIFIER_TYPE_LOCAL = 4;
    
    def __init__(self,prevStack=None):
        self.stack  = []; #last element in array is always top of stack.
        self.endNames = {};
        
        if prevStack != None:
            for ctx in prevStack.stack:
                self.stack.append(ctx);

            self.endNames = prevStack.endNames;
            
    def addEndpointName(self,endName):
        self.endNames[endName] = True;
        
    def isEndpointName (self,toTest):
        val = self.endNames.get(toTest,None);
        if val == None:
            return False;
        return True;

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


    def addToVarReadSet(self,nodeName,ntt):
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
            curFuncDep.addToVarReadSet(nodeName,ntt);

    def addReadsToVarReadSet(self,nodeName,reads):
        '''
        If we are inside of a function, then tell the function that
        variable with name nodeName relies on reads and writes from
        the NodeNameTuples populating the arrays reads and writes.
        '''
        topStack = self.checkStackLen('addReadsWritesToVarReadSet');
        curFuncDep = topStack.currentFunctionDep;
        if curFuncDep != None:
            # happened inside a function instead of happening
            # inside of an endpoint global section.
            curFuncDep.addReadsToVarReadSet(nodeName,reads);

    def addRead(self,ntt):
        '''
        If we are inside of a function, then tell the function that
        the function relies on the attached ntt.
        '''
        topStack = self.checkStackLen('addReadsWritesToVarReadSet');
        topStack.addRead(ntt);
            
        
        
    def getReadIndex(self):
        '''
        @see getReadIndex of Context
        '''
        stackTop = self.checkStackLen('getReadIndex');
        return stackTop.getReadIndex();

    def getWriteIndex(self):
        '''
        @see getReadIndex of Context
        '''
        stackTop = self.checkStackLen('getWriteIndex');
        return stackTop.getWriteIndex();

    def getReadsAfter(self,afterPoint):
        '''
        @see getReadIndex of Context
        '''
        stackTop = self.checkStackLen('getReadsAfter');
        return stackTop.getReadsAfter(afterPoint);
    
    def getWritesAfter(self,afterPoint):
        '''
        @see getReadIndex of Context
        '''
        stackTop = self.checkStackLen('getWritesAfter');
        return stackTop.getWritesAfter(afterPoint);

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
        self.reads = [];
        self.writes = [];
        self.labelAs = labelAs;
        self.currentFunctionDep = currentFunctionDep;


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

    
    def getWriteIndex(self):
        '''
        @see getReadIndex
        '''
        return len(self.writes);

    def getWritesAfter(self,afterPoint):
        '''
        @see getReadIndex
        '''        
        return self.writes[afterPoint:];
        
    def addRead(self,ntt):
        self.reads.append(ntt);

        if self.currentFunctionDep != None:
            # happened inside a function instead of happening
            # inside of an endpoint global section.
            self.currentFunctionDep.addFuncReads([ntt]);

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

    
    def getWriteIndex(self):
        '''
        @see getReadIndex
        '''
        return len(self.writes);

    def getWritesAfter(self,afterPoint):
        '''
        @see getReadIndex
        '''        
        return self.writes[afterPoint:];
        
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

    
class NameTypeTuple(object):
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
        
        if ((argPosition != None) and
            (varType != TypeStack.IDENTIFIER_TYPE_FUNCTION_ARGUMENT)):
            errMsg = '\nBehram error: should not receive an arg position ';
            errMsg += 'with a variable that is not a function argument.\n';
            print(errMsg);
            assert(False);

        self.argPosition = argPosition;

    def mark(self):
        self._mark = True;
    def unmark(self):
        self._mark = False;
    def isMarked(self):
        return self._mark;
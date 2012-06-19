#!/usr/bin/python

import sys;
from  astLabels import *;
import json;

OutputErrsTo = sys.stderr;

def isFunctionType(typeLabel):
    '''
    Nodes can have many different type labels.  Some are specified by
    strings (mostly nodes with basic types, eg. Number, String, etc.).

    Nodes for user-defined function types do not just have one
    annotation, but rather a json-ized type.  To check if a node's
    label is one of these user-defined function types, we check to
    exclude all of the other types it could be.

    Returns true if it is a user-defined function type, false otherwise.
    
    '''
    
    if ((typeLabel != TYPE_BOOL) and (typeLabel != TYPE_NUMBER) and
        (typeLabel != TYPE_STRING) and (typeLabel != TYPE_INCOMING_MESSAGE) and
        (typeLabel != TYPE_OUTGOING_MESSAGE) and (typeLabel != TYPE_NOTHING)):

        jsonType = json.loads(typeLabel);
        if (jsonType.get('Type',None) == None):
            errMsg = '\nBehram error.  got a json object that did not have ';
            errMsg += 'a type field.\n';
            print(errMsg);
            assert (False);
            
        if (jsonType['Type'] == TYPE_FUNCTION):
            return True;

    return False;


def isTemplatedType(typeLabel):
    '''
    @returns{bool} True if it's a function or list type, false otherwise.
    '''
    if ((typeLabel != TYPE_BOOL) and (typeLabel != TYPE_NUMBER) and
        (typeLabel != TYPE_STRING) and (typeLabel != TYPE_INCOMING_MESSAGE) and
        (typeLabel != TYPE_OUTGOING_MESSAGE) and (typeLabel != TYPE_NOTHING)):
        return True;

    return False;


def setOutputErrorsTo(toOutputTo):
    global OutputErrsTo;
    OutputErrsTo = toOutputTo;

def errPrint(toPrint):
    '''
    @param{String} toPrint
    Outputs toPrint on stderr
    '''
    global OutputErrsTo;
    print >> OutputErrsTo , toPrint;



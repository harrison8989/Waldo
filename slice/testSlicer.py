#!/usr/bin/env python

import sys;
import os;

curDir = os.path.dirname(__file__);
sys.path.append(os.path.join(curDir,'..','bin'));

import head;
from slicer import slicer;


class StreamObj(object):
    def __init__(self):
        self.msg = '';
    def write(self,msg):
        self.msg += msg;
    def flush(self):
        msg = self.msg;
        self.msg = '';
        return msg;

def run (filename):
    filer = open(filename,'r');
    progText = filer.read();
    filer.close();
    
    outputErrStream = StreamObj();
    rootNode = head.lexAndParse(progText,outputErrStream,2);

    if rootNode == None:
        print('\nErrors encountered\n');
        print (outputErrStream.flush());
        return;

    fDeps = slicer(rootNode);

    # turn fDeps into a dictionary
    warnMsg = '\nBehram warn.  Need to add endpoint information ';
    warnMsg += 'to each function name in fDeps to ensure that when ';
    warnMsg += 'turn into a dictionary, do not overwrite the function ';
    warnMsg += 'of one endpoint with that of another.\n';
    print(warnMsg);
    allDepsDict = {};
    for dep in fDeps:
        allDepsDict[dep.funcName] = dep;
    
    print('\n\n');
    for dep in fDeps:
        print(dep.jsonize(allDepsDict));
        print('\n');
    print('\n\n');
        
        
if __name__ == '__main__':
    run(sys.argv[1]);

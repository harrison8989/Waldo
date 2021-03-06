import time
import sys
sys.path.append("../../../")
from waldo.lib import Waldo
from emitted import Server
import subprocess
import random
import string

numMessages = 1000
numClients = 1

if(len(sys.argv) >= 2):
        rewrite = sys.argv[1]
else:
        rewrite = raw_input('Overwrite logs? (Input y/n): ')
if(rewrite in ['y', 'Y']):
        f = open('clientLog', 'w')
else:
        f = open('clientLog', 'a')

def display_msg(endpoint, msg):
        '''
        Signalling message. Does nothing.
        '''
        pass

def nothing(endpoint):
        '''
        Signalling message. Does nothing.
        '''
        pass

server = Waldo.no_partner_create(Server, display_msg, nothing)
for i in range(0,1):
    mult = 0
    if i == -2:
        print 'Started'
        startTime = time.time()
        for j in range(0,numMessages):
            #call server.nothing() to have a truly null message (i==-1 has a
            #null string message)
            server.nothing()
        totalTime = time.time() - startTime
        print 'Finished: ' + str(totalTime)

    else:
        if i == -1:
            mult = 0
        else:
            mult = 2**i

        texts = []
        for i in range(0,numMessages):
                texts.append(''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(mult*3)))
        #print texts

        print 'Started'
        startTime = time.time()

        for text in texts:
            server.display_msg(text)

        totalTime = time.time() - startTime
        print 'Finished: ' + str(totalTime)
    f.write(str(i) + ' ' + str(numMessages) + ' ' + str(totalTime) + '\n')

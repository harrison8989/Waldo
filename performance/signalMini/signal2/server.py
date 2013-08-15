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
        #print msg
        pass

def nothing(endpoint):
        '''
        Signalling message. Does nothing.
        '''
        pass

server = Waldo.no_partner_create(Server, display_msg, nothing)
print 'Started'
startTime = time.time()

for j in range(0,numMessages):
        server.sendMSG(str(j),1)
        #server.sendMSG(str(j),1)

totalTime = time.time() - startTime
print 'Finished: ' + str(totalTime)

f.write(str(1) + ' ' + str(numMessages) + ' ' + str(totalTime) + '\n')

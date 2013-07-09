from chatroom import Server
from manager import Manager
import time
import sys
sys.path.append("../..")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 7937
startTime = 0
f = open('serverLog', 'w')

m = Waldo.no_partner_create(Manager)
numMessages = 1000
numConnected = 0

def connected(endpoint):
        '''
        connected_callback function when server connects
        '''
        global numConnected
        numConnected += 1


Waldo.tcp_accept(Server, HOSTNAME, PORT, m, connected_callback = connected)
print 'Server is running. Better go catch it!'

while numConnected < 17:
        if numConnected:
                print 'Started'
                startTime = time.time()
                for i in range(0, numMessages):
                        m.broadcast(str(i))
                f.write(str(numConnected * numMessages) + ' ' + str(time.time() - startTime) + '\n')
                print 'Finished'

from emitted import Server
import subprocess
import time
import sys
sys.path.append("../../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
SLEEPTIME = .001
COUNTERREFRESH = 10000
numMessages = 1000
startTime = 0
timeout = 5
numKilled = 0
numClients = 0

#The server.py now manages the client files too. This improves coordination
#while still leaving multiprocessing features.

if(len(sys.argv) >= 2):
        rewrite = sys.argv[1]
else:
        rewrite = raw_input('Overwrite logs? (Input y/n): ')
if(rewrite in ['y', 'Y']):
        f = open('clientLog', 'w')
        f.close()
        f = open('serverLog', 'w')
else:
        f = open('serverLog', 'a')
n = 1

def display_msg(endpoint, msg):
        '''
        Called when a client sends a message to the server.
        Misleading function name: display_msg doesn't actually display a msg.
        '''
        global f
        global n
        global startTime
        if(msg == str(numMessages - 1)):
                f.write(str(n) + ' ')
                n += 1
                f.write(str(time.time() - startTime) + '\n')



Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg)

print 'Server is up and running.'

for i in range(1, 2):
        numClients = i
        for k in range(0, i):
                subprocess.Popen(["python","client.py ",str(i)])

        #wait for endpoints to die...
        time.sleep(10)

        numKilled = 0

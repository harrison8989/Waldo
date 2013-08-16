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

def connected(endpoint):
        '''
        Called when a client connects to the server.
        '''
        global timeout
        global numKilled
        global numClients
        global startTime
        counter = 0
        startTime = time.time()


        while True:
                endpoint.service_signal()
                counter += 1

                if counter % COUNTERREFRESH == 0:
                        if time.time() - startTime > numClients * timeout:
                                numKilled += 1
                                break
                                #todo:
                                #have the client only send new messages after
                                #this time has been finished (to prevent
                                #overlap
                                #ghetto solution
                #because of this queue, something is still running...
                #the service_signal is making something last longer
                #like it's not being destroyed properly
                #
                #Never mind, the connected_callback needs to be
                #destroyed when the endpoint is disconnected

Waldo.tcp_accept(Server, HOSTNAME, PORT, connected_callback = connected)

print 'Server is up and running.'

for i in range(1, 2):
        numClients = i
        for k in range(0, i):
                subprocess.Popen(["python","client.py ",str(i)])

        #wait for endpoints to die...
        while(numKilled < numClients):
                time.sleep(5)

        numKilled = 0

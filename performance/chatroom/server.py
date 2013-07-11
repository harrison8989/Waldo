from emitted import Server
import subprocess
import time
import sys
sys.path.append("../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
SLEEPTIME = .001
numMessages = 1000
startTime = 0
timeout = 10
numKilled = 0
numClients = 0

if(len(sys.argv) >= 2):
        timeOut = sys.argv[1]

f = open('clientLog', 'w')
f.close()
f = open('serverLog', 'w')
n = 1

def connected(endpoint):
        global timeout
        global numKilled
        global numClients
        print 'Started'
        startTime = time.time()
        counter = 0
        while True:
                endpoint.service_signal()
                counter += 1
                if counter % 1000 == 999:
                        if time.time() - startTime > numClients * timeout:
                                numKilled += 1
                                endpoint.stop()
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

def display_msg(endpoint, msg):
        global f
        global n

        if(msg == str(numMessages - 1)):
                f.write(str(n) + ' ')
                n += 1
                f.write(str(time.time() - startTime) + '\n')
                print "Ended: " + str(time.time() - startTime) + '\n'



Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg, connected_callback = connected)

print 'Server is up and running.'

for i in range(1, 3):
        numClients += 1
        for k in range(0, i):
                subprocess.Popen("python client.py " + str(i))

        #wait for endpoints to die...
        while(numKilled < i):
                time.sleep(5)


        numKilled = 0

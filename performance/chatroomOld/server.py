from emitted import Server
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo/")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
SLEEPTIME = .001
numMessages = 1000

startTime = time.time()
f = open('serverLog', 'w')
n = 1

def connected(endpoint):
        global startTime
        global f
        global n
        print 'Started'
        startTime = time.time()
        while True:
                pass
                #endpoint.service_signal()
                #because of this queue, something is still running...
                #the service_signal is making something last longer
                #like it's not being destroyed properly

def display_msg(endpoint, msg):
        global f
        global n
	#print time.time() - startTime

        if(msg == str(numMessages - 1)):
                f.write(str(n) + ' ')
                n += 1
                f.write(str(time.time() - startTime) + '\n')
                print "Ended: " + str(time.time() - startTime) + '\n'


Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg, connected_callback = connected)

print 'Server is up and running.'
while True:
	pass

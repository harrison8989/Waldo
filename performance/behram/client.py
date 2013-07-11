#!/usr/bin/env python
from emitted import Client
import sys
import time
sys.path.append("../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 10000

f = open('clientLog', 'w')

for i in range(1,100000):
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)

        print 'Started'
        f.write(str(i) + ' ' + str(numMessages) + ' ')
        startTime = time.time()

        stop_except = False
        try:
                for n in range(0, numMessages):
                        client.send_msg(str(n))
        except Waldo.StoppedException:
                print '\nReceived stop and closing\n'
                stop_except = True

        f.write(str(time.time() - startTime) + '\n')
        print "Finished: " + str(time.time() - startTime) + '\n'

        #if stop_except:
        #        break
        
f.close()

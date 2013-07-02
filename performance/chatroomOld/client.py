from emitted import Client
import sys
import time
sys.path.append("C:/Users/perceptual/Waldo/")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 1000

f = open('clientLog', 'w')

for i in range(1,17):
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)

        print 'Started'
        f.write(str(i) + ' ' + str(numMessages) + ' ')
        startTime = time.time()

        for n in range(0, numMessages):
                client.send_msg(str(n))

        f.write(str(time.time() - startTime) + '\n')
        print "Finished: " + str(time.time() - startTime) + '\n'

        client.stop()

f.close()

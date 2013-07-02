from emitted import Client
import sys
import time
sys.path.append("C:/Users/perceptual/Waldo/")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 9028

f = open('clientLog', 'w')

for i in range(0,16):
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)
        client2 = Waldo.tcp_connect(Client, HOSTNAME, PORT)

        print 'Started'
        f.write(str(i) + ' ')
        startTime = time.time()

        for n in range(0, 1000):
                client.send_msg(str(n))
                client2.send_msg(str(n))

        f.write(str(time.time() - startTime) + '\n')
        print "Finished: " + str(time.time() - startTime) + '\n'

f.close()

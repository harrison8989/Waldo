import sys
sys.path.append("C:/users/perceptual/waldo")
from waldo.lib import Waldo
from emitted import Ping
import time

numMessages = 1000

f = open('clientLog', 'w')
pingers = []

for i in range(1,17):

    ping = Waldo.tcp_connect(Ping, '127.0.0.1', 6767)
    pingers.append(ping)

    print 'Started'
    startTime = time.time()

    for p in pingers:
        for i in range(0, numMessages):
            p.ping_seq(i)

    print "Finished: " + str(time.time() - startTime) + '\n'
    f.write(str(i) + " " + str(i * numMessages) + " " + str(time.time() - startTime) + '\n')

from emitted import Client
import sys
import time
sys.path.append("../../")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 1000

#f = open('clientLog', 'a')

client = Waldo.tcp_connect(Client, HOSTNAME, PORT)

print 'Started'
#f.write(str(i) + ' ' + str(numMessages) + ' ')
startTime = time.time()

for n in range(0, numMessages):
        client.send_msg(str(n))

#f.write(str(time.time() - startTime) + '\n')
totalTime = time.time() - startTime
print "Finished: " + str(totalTime) + '\n'

f = open('clientLog', 'a')
numClients = 0
if(len(sys.argv) >= 2):
        numClients = sys.argv[1]

f.write(str(numClients) + ' ' + str(numMessages) + ' ' + str(totalTime) + '\n')


#f.close()

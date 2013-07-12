from emitted import Client
import sys
import time
sys.path.append("../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 1000

client = Waldo.tcp_connect(Client, HOSTNAME, PORT)

print 'Started'
startTime = time.time()

try {
        for n in range(0, numMessages):
                client.send_msg(str(n))
} catch {


}
print "Finished: " + str(time.time() - startTime) + '\n'

f = open('clientLog', 'a')
numClients = 1
if(len(sys.argv) >= 2):
        #assume numClients is only one unless the number of clients is given
        numClients = int(sys.argv[1])

f.write(str(numClients) + ' ' + str(numClients * numMessages) + ' ' + str(totalTime) + '\n')
client.stop()


f.close()

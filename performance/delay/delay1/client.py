from emitted import Client
import sys
import time
sys.path.append("../../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 1000
DELAY = 10

def main():
        #Connecting + Starting
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)
        print 'Started'
        startTime = time.time()


        #Sending all messages
        try:
                for n in range(0, 100):
                        client.send_msg(str(100))
			time.sleep(DELAY)
                for n in range(100, numMessages):
                        client.send_msg(str(n))
			time.sleep(DELAY)
        except:
                print 'Sending message failed.'


        #Packaging time and sending it
        totalTime = time.time() - startTime
        print "Finished: " + str(totalTime)
        numClients = 1
        if(len(sys.argv) >= 2):
                #assume numClients is only one unless the number of clients is given
                numClients = int(sys.argv[1])


        #Writing and closing
        client.stop()
        f = open('clientLog', 'a')
        f.write(str(numClients) + ' ' + str(numClients * numMessages) + ' ' + str(totalTime) + '\n')
        f.close()

main()

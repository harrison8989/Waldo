from emitted import Client
import sys
import time
sys.path.append("../../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 1000

def main():
        #Connecting + Starting
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)
        print 'Started'

        #preparing the string lengths
        length = 0
        if(len(sys.argv) >= 2):
                length = int(sys.argv[1])
        if length == -1:
                mult = 0
        else:
                mult = 2**length
        texts = []
        for i in range(0,mult):
                texts.append('123')

        startTime = time.time()


        #Sending all messages
        try:
                for i in range(0,numMessages):
                        client.send_msg(texts)
        except:
                print 'Sending message failed.'


        #Packaging time and sending it
        totalTime = time.time() - startTime
        client.send_msg(str(numMessages - 1)) #final message to signal to server
        print "Finished: " + str(totalTime)

        #Writing and closing
        client.stop()
        f = open('clientLog', 'a')
        f.write(str(length) + ' ' + str(numMessages) + ' ' + str(totalTime) + '\n')
        f.close()

main()

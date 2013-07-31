from emitted import Client
import sys
import time
sys.path.append("../../../")
from waldo.lib import Waldo
import random
import string

HOSTNAME = '127.0.0.1'
PORT = 9028
numMessages = 1000

def main():
        #Connecting + Starting
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)
        print 'Started'

        #preparing the string lengths
        power = 0
        if(len(sys.argv) >= 2):
                power = int(sys.argv[1])
        mult = 2**power
        texts = []

        for i in range(0,numMessages):
                texts.append(''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(mult*3)))
        print texts

        startTime = time.time()

        #Sending all messages
        try:
                for text in texts:
                        client.send_msg(text)
        except:
                print 'Sending message failed.'


        #Packaging time and sending it
        totalTime = time.time() - startTime
        client.send_msg(str(numMessages - 1)) #final message to signal to server
        print "Finished: " + str(totalTime)

        #Writing and closing
        client.stop()
        f = open('clientLog', 'a')
        f.write(str(power) + ' ' + str(numMessages) + ' ' + str(totalTime) + '\n')
        f.close()

main()

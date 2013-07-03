from chatroom import Client
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from waldo.lib import Waldo
import time

HOSTNAME = '127.0.0.1'
PORT = 7937
startTime = 0
f = open('clientLog', 'w')
numClients = 1;
numMessages = 1000
hit = False

def getMSG(endpoint, msg):
        global startTime
        global c
        global numClients
        global hit
        if msg == '0':
                hit = False
                print 'start'
                startTime = time.time()
        if msg == '999' and not hit:
                f.write(str(numClients) + ' ' + str(numClients * numMessages) + ' ' + str(time.time() - startTime) + '\n')
                print time.time() - startTime
                print 'finished'
                numClients += 1
                client = Waldo.tcp_connect(Client, HOSTNAME, PORT, getMSG)
                c.append(client)
                hit = True

client = Waldo.tcp_connect(Client, HOSTNAME, PORT, getMSG)
c = []
c.append(client)

while True:
        for cl in c:
                cl.service_signal()

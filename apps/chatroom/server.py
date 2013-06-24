from emitted import Server
from Tkinter import *
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 8195
count = [0,0,0]
full = ["Bang!", "Kill Dr. Lucky", "Sitting Ducks"]
msgs = []
REFRESH = .1

def connected(endpoint):
	while True:
		time.sleep(REFRESH)
		endpoint.service_signal()
                endpoint.receiveStatus(count)

def display_msg(endpoint, msg):
	if(msg != ''):
                print(msg)
                msgs.append(msg)
        #msgPos += 1
        #if(len(msgs) >= 1000):
        #        msgs[msgPos % 1000] = msg
        #else:
        #endpoint.addMSG(msg)
        endpoint.changeMSGS(msgs) #I think I should make updating a separate function
        #print endpoint.getMSGS()
        #print msgs

        #endpoint.send_msg(msg)


def vote(endpoint, gameNum, enter):
	if(gameNum >= 0):
		increment = -1
		if enter:
			increment = 1
		count[int(gameNum)] += increment


Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg, vote, connected_callback = connected)
print 'Server is up and running.'
while True:
	pass

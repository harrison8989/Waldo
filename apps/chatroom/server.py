from emitted import Server
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 8195
count = [0,0,0]
full = ["Bang!", "Kill Dr. Lucky", "Sitting Ducks"]


def connected(endpoint):
	while True:
#		temp = [0,0,0]
#		endpoint.alertClient(count)
#		for i in range(len(count)):
#			temp[i] = count[i]
		time.sleep(.5)
#		for i in range(len(count)):
#			if(temp[i] != count[i] and count[i] >= 2):
#				endpoint.alertClient(count)
		endpoint.service_signal()
                endpoint.receiveStatus(count)

def display_msg(endpoint, msg):
	print(msg)

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

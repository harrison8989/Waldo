from emitted import Server
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]
count = [0,0,0]
full = ["Bang!", "Kill Dr. Lucky", "Sitting Ducks"]


def connected(endpoint):
	while True:
		temp = [0,0,0]
		for i in range(len(count)):
			temp[i] = count[i]
		endpoint.service_signal()
		for i in range(len(count)):
			if(temp[i] != count[i] and count[i] >= 2):
				endpoint.alertClient(count)
		time.sleep(.5)
		#print count

def display_msg(endpoint, msg):
	print(msg)
	
def vote(endpoint, gameNum, enter):
	if(gameNum >= 0):
		increment = -1
		if enter:
			increment = 1
		count[int(gameNum)] += increment
	

for num in PORT:
	Waldo.tcp_accept(Server, HOSTNAME, num, display_msg, vote, connected_callback = connected)
print 'Server is up and running.'
while True:
	pass



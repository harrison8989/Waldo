from chatroom import Server
from manager import Manager
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

m = Waldo.no_partner_create(Manager)

def connected(endpoint):
        '''
        connected_callback function when server connects
        '''
        endpoint.changeMSGS(msgs)
	while True:
		time.sleep(REFRESH)
		endpoint.service_signal()
                endpoint.receiveStatus(count)

def display_msg(endpoint, msg):
        '''
        display message, also updates list of messages
        '''
	if(msg != ''):
                print(msg)
                msgs.append(msg)
        endpoint.changeMSGS(msgs) #I think I should make updating a separate function


def vote(endpoint, gameNum, enter):
        '''
        vote function used by client
        '''
	if(gameNum >= 0):
		increment = -1
		if enter:
			increment = 1
		count[int(gameNum)] += increment


Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg, vote, m, connected_callback = connected)
print 'Server is up and running.'
while True:
	pass

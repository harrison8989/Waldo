from emitted import Server
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo/")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 8643

server = 0
def connected(endpoint):
	print server
	#assert (False)
	while True:
		endpoint.service_signal()
		time.sleep(.5)

def display_msg(endpoint, msg):
	print(msg)


Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg, connected_callback = connected)

print 'Server is up and running.'
while True:
	pass



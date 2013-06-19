from emitted import Server
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 6983
CERTIFICATE = 'my certificate lolz'

def connected(endpoint):
	print 'We have liftoff\n'
	endpoint.setCert(CERTIFICATE);
	while True:
		endpoint.service_signal()
		time.sleep(.5)
		print "snore"

def display_msg(endpoint, msg):
	print('MSG: ' + msg)
	
Waldo.tcp_accept(Server, HOSTNAME, PORT, display_msg, connected_callback = connected)
print 'Server is up and running.'
while True:
	pass



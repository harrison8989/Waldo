from emitted import Server
import time
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009]


def connected(endpoint):
	while True:
		endpoint.service_signal()
		time.sleep(.5)
		#print count

def display_msg(endpoint, msg):
	print(msg)

for num in PORT:
	Waldo.tcp_accept(Server, HOSTNAME, num, display_msg, connected_callback = connected)
print 'Server is up and running.'
while True:
	pass



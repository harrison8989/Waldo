from emitted import Client
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 6983

def display_msg(endpoint, msg):
	print('MSG: ' + msg)


client = Waldo.tcp_connect(Client, HOSTNAME, PORT, display_msg)
print 'liftoff!\n'
result = client.startSeq()


if int(result / 1000) == 1:
	print 'Server is ready!\n'
else:
	print 'Server is not ready.\n'
if int(result / 100) % 10 == 1:
	print 'Client is ready!\n'
else:
	print 'Client is not ready.\n'
	
	
while True:
	msg_to_send = raw_input('Say something: ')
	client.send_msg(msg_to_send)

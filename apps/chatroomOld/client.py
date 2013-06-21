from emitted import Client
import sys
sys.path.append("C:/Users/perceptual/Waldo/")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 8643

name = raw_input('What is your name? ')
client = Waldo.tcp_connect(Client, HOSTNAME, PORT, name)

print 'liftoff!\n'

while True:
	msg_to_send = raw_input('Say something: ')
	if(msg_to_send != ''):
		client.send_msg(name + ": " + msg_to_send)

from emitted import Client
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
HOSTNAME = '127.0.0.1'

port = raw_input('Enter port: ')
name = raw_input('What is your name? ')
client = Waldo.tcp_connect(Client, HOSTNAME, port, name)

print 'liftoff!\n'

while True:
	msg_to_send = raw_input('Say something: ')
	client.send_msg(name + ": " + msg_to_send)

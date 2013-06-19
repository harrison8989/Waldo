from emitted import Client
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
HOSTNAME = '127.0.0.1'
myGame = -1;
games = ["bang","lucky","ducks"]
full = ["Bang!", "Kill Dr. Lucky", "Sitting Ducks"]
count = [0,0,0]
EXITSTRING = "exit"

def switch(msg):
	if msg in games:
		return {
			"bang": 0,
			"lucky": 1,
			"ducks": 2,
		}[msg]
	if msg == EXITSTRING:
		return -2
	return -1

def getData(endpoint, data):
	if(data[myGame] >= 2):
		print full[myGame] + ' is ready!'

port = raw_input('Enter port: ')
name = raw_input('What is your name? ')
client = Waldo.tcp_connect(Client, HOSTNAME, port, getData, name)

print 'liftoff!\n'

	
while True:
	client.service_signal()
	#print count
	msg_to_send = raw_input('Say something: ')
	if(msg_to_send != ''):
		if(msg_to_send[0] != '/'):
			client.send_msg(name + ": " + msg_to_send)
		else:
			result = switch(msg_to_send[1:])
			if(result != myGame):
				client.send_cmd(myGame, False)
				if(myGame >= 0):
					client.send_msg(name + " no longer wishes to play " + full[myGame] + ". Sissy.")
				if(result >= 0):
					client.send_cmd(result, True)
					client.send_msg(name + " would like to play " + full[result] + "!")
			
			myGame = result;

from emitted import Client
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 8195
myGame = -1;
games = ["bang","lucky","ducks"]
full = ["Bang!", "Kill Dr. Lucky", "Sitting Ducks"]
count = [0,0,0]
EXITSTRING = "exit"
QUITSTRING = "quit"
UPDATESTRING = "up"

def switch(msg):
	if msg in games:
		return {
			"bang": 0,
			"lucky": 1,
			"ducks": 2,
			EXITSTRING: -2,
			QUITSTRING: -3,
                        UPDATESTRING: -4
		}[msg]
	return -1

def getData(endpoint, data):
	if(data[myGame] >= 2):
		print full[myGame] + ' is ready!'

name = raw_input('What is your name? ')
client = Waldo.tcp_connect(Client, HOSTNAME, PORT, getData, name)

print 'liftoff!\n'
client.send_msg(name + ' has connected.')

while True:
        ready = client.send_cmd(-3, False)
        if ready:
                print full[myGame] + " is ready to play!"
	msg_to_send = raw_input('Say something: ')
	if(msg_to_send != ''):
		if(msg_to_send[0] != '/'):
			client.send_msg(name + ": " + msg_to_send)
		else:
			result = switch(msg_to_send[1:])
			if(result != myGame):
				if(result == -3):
					Waldo.stop(); #does this even work?
				else:
					client.send_cmd(myGame, False)
					if(myGame >= 0):
						client.send_msg(name + " no longer wishes to play " + full[myGame] + ". Sissy.")
					if(result >= 0):
						client.send_cmd(result, True)
						client.send_msg(name + " would like to play " + full[result] + "!")
                                                client.setGame(result)

			myGame = result;

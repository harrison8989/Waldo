import time
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
from emitted import ChatterA, ChatterB
HOSTNAME = '127.0.0.1'
PORT = 6922
name = ''

def display_msg(endpoint,msg):
    # note: a more sophisticated app might write to a gui instead.
    print (msg)

	
def run_chatter_a():
    # runs in accept mode
	name = raw_input('Input name: ')
	#print name
	Waldo.tcp_accept(
		ChatterA, HOSTNAME, PORT, display_msg, name,
		connected_callback = listen_for_other_side)
	while True:
		pass

def run_chatter_b():
    name = raw_input('Input name: ')
    #print name
    chatter_b = Waldo.tcp_connect(
        ChatterB, HOSTNAME, PORT, display_msg, name)
    listen_for_other_side(chatter_b)

def listen_for_other_side(endpoint_obj):
	'''
	Continuously poll to see if there's a message from other side to display.
	'''
	while(True):
		num = endpoint_obj._signal_queue.qsize()
		for i in range(num):
			endpoint_obj.service_signal()
		msg_to_send = raw_input('Me: ')
		endpoint_obj.send_msg_to_other_side(msg_to_send)
		time.sleep(.1)

if __name__ == '__main__':
    '''
    Passing in argument 'a' starts ChatterA listening.

    Executing another process passing in 'b' starts ChatterB taking input from user.
    '''
    if (sys.argv[1] == 'a'):
       run_chatter_a()
    else:
       run_chatter_b()
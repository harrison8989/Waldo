import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
from emitted import Pong
import time
import subprocess

def pong_connected(endpoint):
	print '\nPong endpoint is connected!\n'
	endpoint.changeText("pong: " + subprocess.check_output("pwd"))


Waldo.tcp_accept(
    Pong, 'localhost',6767, connected_callback=pong_connected)
for i in range(1,10):
	print i
	time.sleep(1)
 
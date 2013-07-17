import sys
sys.path.append("../..")
from waldo.lib import Waldo
from emitted import Pong
import time

def pong_connected(endpoint):
    print '\nPong endpoint is connected!\n'

Waldo.tcp_accept(
    Pong, 'localhost',6767, connected_callback=pong_connected)

print 'Server is running. Better go catch it!'

while True:
    pass

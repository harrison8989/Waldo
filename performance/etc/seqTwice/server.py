from emitted import Server
import sys
sys.path.append("../../../")
from waldo.lib import Waldo
import time

HOSTNAME = '127.0.0.1'
PORT = 9028


Waldo.tcp_accept(Server, HOSTNAME, PORT)

print 'Server is up and running.'

while True:
    pass
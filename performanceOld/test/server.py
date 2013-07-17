from emitted import Server
import subprocess
import time
import sys
sys.path.append("../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9876
DELAY = .001

def connected(endpoint):
        while True:
                endpoint.service_signal()

Waldo.tcp_accept(Server, HOSTNAME, PORT, connected_callback = connected)

print 'Server is up and running.'

for i in range(1, 17):
        subprocess.Popen("python client.py ")
        time.sleep(DELAY)

while True:
        pass

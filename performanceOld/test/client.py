from emitted import Client
import sys
import time
sys.path.append("../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9876

def main():
        client = Waldo.tcp_connect(Client, HOSTNAME, PORT)
        print 'Started'
        time.sleep(5)
        client.stop()

main()

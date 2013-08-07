from emitted import Client
import sys
sys.path.append("../../../")
from waldo.lib import Waldo

HOSTNAME = '127.0.0.1'
PORT = 9028

client = Waldo.tcp_connect(Client, HOSTNAME, PORT)
client.send_msg('100')
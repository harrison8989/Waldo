import sys
sys.path.append("C:/Users/perceptual/Waldo")
from lib import Waldo
from emitted import Ping
import time
import subprocess

ping = Waldo.tcp_connect(Ping, 'localhost', 6767)

ping.changeText("ping: "+subprocess.check_output("pwd"))
print (str(ping.ping_seq('')))
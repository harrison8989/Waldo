import time
import subprocess

f = open('clientLog', 'w')
f.close()

servTimeOut = 10
clientTimeOut = 15

server = subprocess.Popen("python server.py " + str(servTimeOut))
for i in range(0, 2):
    for k in range(0, i):
        subprocess.Popen("python client.py " + str(i))
    time.sleep(clientTimeOut * i)

server.kill()

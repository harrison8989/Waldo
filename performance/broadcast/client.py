from chatroom import Client
from Tkinter import *
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 7937

def getMSG(endpoint, msg):
        print msg

client = Waldo.tcp_connect(Client, HOSTNAME, PORT, getMSG)

def cb(event):
        callback()

def callback():


#print 'liftoff!\n'
client.send_msg(name + ' has connected.')



def task(ready):
        thing = client.service_signal()

        root.after(REFRESH,lambda:task(ready))

root.after(REFRESH,lambda:task(ready))
root.mainloop()

from emitted import Client
from Tkinter import *
import sys
sys.path.append("C:/Users/perceptual/Waldo")
from waldo.lib import Waldo
HOSTNAME = '127.0.0.1'
PORT = 8195
games = ["bang","lucky","ducks"]
full = ["Bang!", "Kill Dr. Lucky", "Sitting Ducks"]
count = [0,0,0]
EXITSTRING = "exit"
QUITSTRING = "quit"
UPDATESTRING = "up"
REFRESH = 100
myGame = -1
ready = False

retrieve = 0

def switch(msg):
	if msg in games:
		return {
			"bang": 0,
			"lucky": 1,
			"ducks": 2,
			EXITSTRING: -2,
			QUITSTRING: -3,
                        UPDATESTRING: -4
		}[msg]
	return -1



def getData(endpoint, data):
        pass
        #if(data[myGame] >= 2 and myGame >= 0):
                #print full[myGame] + ' is ready!'

def getMSG(endpoint, msg):
        listbox.insert(END, msg)
        listbox.yview(END)
        #print msg



name = raw_input('What is your name? ')


#gui stuff

root = Tk()
root.geometry("500x220")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(side=TOP, fill=BOTH)
scrollbar.config(command=listbox.yview)

e = Entry(root,width=100)
e.pack()
e.focus_set()

#client stuff

client = Waldo.tcp_connect(Client, HOSTNAME, PORT, getData, getMSG, name)

def cb(event):
        callback()

def callback():
        myGame = int(client.getGame())
        msg_to_send = e.get()
        ready = client.send_cmd(-3, False)
        #if ready:
                #print full[myGame] + " is ready to play!"

	if(msg_to_send != ''):
                e.delete(0,END)
                listbox.yview(END)

		if(msg_to_send[0] != '/'):
			client.send_msg(name + ": " + msg_to_send)

		else:
                        #print msg_to_send[1:]
			result = switch(msg_to_send[1:])
                        #print "My game is " + str(myGame)

			if(result != myGame):
				if(result == -3):
					Waldo.stop(); #does this even work? i don't think so!
				else:
					client.send_cmd(myGame, False)
					if(myGame >= 0):
						client.send_msg(name + " no longer wishes to play " + full[myGame] + ". Sissy.")
					if(result >= 0):
						client.send_cmd(result, True)
						client.send_msg(name + " would like to play " + full[result] + "!")
                                                #client.setGame(result)
                        client.setGame(result)
			myGame = result;

b = Button(root, text="Enter", width=10, command=callback)
b.pack(side=BOTTOM)
e.bind('<Return>',cb)


#print 'liftoff!\n'
client.send_msg(name + ' has connected.')



def task(ready):
        client.send_msg('')
        client.retrieveMSG()
        myGame = client.getGame()
        temp = ready
        ready = client.send_cmd(-3, False)
        if temp != ready and ready:
                listbox.insert(END, full[myGame] + " is ready to play!")
                listbox.yview(END)
        thing = client.service_signal()

        root.after(REFRESH,lambda:task(ready))

root.after(REFRESH,lambda:task(ready))
root.mainloop()

import datetime
from datetime import date
import os
import shutil

#Creates a performance.html that quickly aggregates data for viewing pleasure

#maintain this the same as performAll.py (which might be problematic? MEH!)
dirs = [
    'chatroom/chatroom',
    'chatroom/chatroom1',
    'chatroom/chatroom2',
    'chatroom/chatroom3',
    'chatroom/chatroom4',

    'incremental/chatroom',
    'incremental/chatroomA',
    'incremental/chatroomA.1',
    'incremental/chatroomB',
    'incremental/chatroomC',
    'incremental/chatroomD',
    'incremental/chatroomE',
    'incremental/chatroomF',
]

secondaryDir = 'homeTest' #change

def emit():
    f = open('performance.html', 'w')
    f.write('<!DOCTYPE html>\n')
    f.write("<!--AUTOMATICALLY GENERATED -- DON'T EDIT-->\n")
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>Performance Stuff</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    f.write('<h2>Test Bundle: ' + str(date.today()) + '</h2>\n')
    f.write('<h3>Test Name: ' + secondaryDir + '.</h3>\n<hr>\n')

    initDir = os.getcwd()
    #initDir.replace('\\','/')

    for dir in dirs:
        os.chdir(initDir)
        f.write('<h4>Test in directory: ' + dir + '.</h4>')
        os.chdir(dir)
        r = None
        try:
            with open('about.txt', 'r') as about:
                f.write('<ul>\n')
                for line in about:
                    if line[0] == '-':
                        f.write('<li>' + line[1:] + '</li>\n')
                    else:
                        f.write('<li>' + line + '</li>\n')
                f.write('</ul>\n')
        except:
            f.write('<p>No descriptive information was found.</p>')
        os.chdir(secondaryDir)

        #search for the last directory that exists
        counter = 0
        exists = os.path.exists(dir[:3] + str(counter))
        while exists:
            counter += 1
            exists = os.path.exists(dir[:3] + str(counter))
        counter -= 1
        writeSTR = '<img src="' + initDir + '/' + dir + '/' + secondaryDir + '/' + dir[:3] + str(counter) + '/latency.png" height="300" width="600">\n'
        f.write(writeSTR)
        writeSTR = '<img src="' + initDir + '/' + dir + '/' + secondaryDir + '/' + dir[:3] + str(counter) + '/throughput.png" height="300" width="600">\n'
        f.write(writeSTR)
        f.write('<hr>\n')


    f.write('</body>\n')
    f.write('</html>\n')


rewrite = raw_input('Overwrite performance page? (Input y/n): ')
if(rewrite in ['y', 'Y']):
    emit()

print 'Have a nice day!'

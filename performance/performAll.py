import time
import subprocess
import os
import shutil

dirs = {
    'chatroom/chatroom':'plotify3.py',
    'chatroom/chatroom1':'plotify2-5.py',
    'chatroom/chatroom2':'plotify3.py'


}

def main():
    '''
    Runs all performance tests. Assumption is that the only process
    that needs to be called is server.py (that the clients are
    automatically started from the server.)
    '''
    for dir in dirs:
        initDir = os.getcwd()
        os.chdir(dir)

        print '\n\n===============================\n'
        print '---Running test in directory: ' + dir + '\n'
        subprocess.call('python server.py y')
        print '\n---Finished test in directory: ' + dir + '\n'

        print '---Writing and copying data...',

        if not os.path.exists('test'):

            os.makedirs('test')

        counter = 0
        exists = os.path.exists('test/' + dir[:3] + str(counter))
        while exists:
            counter += 1
            exists = os.path.exists('test/' + dir[:3] + str(counter))
        os.makedirs('test/' + dir[:3] + str(counter))

        shutil.copy('clientLog', 'test/' + dir[:3] + str(counter))
        shutil.copy('serverLog', 'test/' + dir[:3] + str(counter))

        os.chdir('test/' + dir[:3] + str(counter))
        subprocess.call('python ' + initDir + '/' + dirs[dir])
        os.chdir(initDir)

        print 'Done!'
        print '\n===============================\n'

main()

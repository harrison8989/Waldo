import time
import subprocess
import os
import shutil

dirs = [
    'chatroom',
    'chatroom'



]
def main():
    '''
    Runs all performance tests. Assumption is that the only process
    that needs to be called is server.py (that the clients are built
    into the system.)
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

        os.chdir(initDir)

        print 'Done!'
        print '\n===============================\n'

main()

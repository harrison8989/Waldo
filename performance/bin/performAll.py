import time
import subprocess
import os
import shutil

#plotify2-5: only one client (but some variable changes over time)
#plotify3: a lot of data that must be averaged, includes error bars
secondaryDir = 'workTest'

def main():
    '''
    Runs all performance tests. Assumption is that the only process
    that needs to be called is server.py (that the clients are
    automatically started from the server.)
    '''
    folders = [] #dunno if this works, let's check it later
    for arg in sys.argv[1:]:
        with open(arg) as dire:
            for dir in dirs:
                folders.append(dir[0:-1])
    if(len(sys.argv) < 2):
        print 'Please input a file containing the directories.'
        return 0

    for folder in folders:
        initDir = os.getcwd()
        os.chdir(folder)

        print '\n\n===============================\n'
        print '---Running test in directory: ' + folder + '\n'
        subprocess.call(['python', 'server.py', 'y'])
        print '\n---Finished test in directory: ' + folder + '\n'

        print '---Writing and copying data...',

        if not os.path.exists(secondaryDir):
            os.makedirs(secondaryDir)

        os.chdir(secondaryDir)
        counter = 0
        exists = os.path.exists(folder[:3] + str(counter))
        while exists:
            counter += 1
            exists = os.path.exists(folder[:3] + str(counter))
        os.makedirs(folder[:3] + str(counter))

        shutil.copy('../clientLog', folder[:3] + str(counter))
        shutil.copy('../serverLog', folder[:3] + str(counter))

        os.chdir(folder[:3] + str(counter))
        subprocess.call(['python', initDir + '/bin/plotify3.py'])
        os.chdir(initDir)

        #just to make sure - be sure to run pypy! taskkill only works
        #on Windows, though
        #hopefully, it will be fine on linux
        if(sys.platform == 'win32' or sys.platform == 'cygwin'):
            subprocess.call('taskkill /im python.exe /f')

        print 'Done!'
        print '\n===============================\n'

main()

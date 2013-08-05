import time
import subprocess
import os
import shutil

#plotify2-5: only one client (but some variable changes over time)
#plotify3: a lot of data that must be averaged, includes error bars

dirs = {
    'sequence/sequence':'plotify3.py',
    'sequence/sequence2':'plotify3.py',
    'sequence/sequence3':'plotify3.py',
    'sequence/sequence4':'plotify3.py',
    'sequence/sequence5':'plotify3.py',

}

secondaryDir = 'workTest'

def main():
    '''
    Runs all performance tests. Assumption is that the only process
    that needs to be called is server.py (that the clients are
    automatically started from the server.)
    '''
    for dir in dirs:
        initDir = os.getcwd()
        os.chdir(dir)
        subprocess.call('python ../../../bin/wcompile.py Sequence.wld')

        print '\n\n===============================\n'
        print '---Running test in directory: ' + dir + '\n'
        subprocess.call('python server.py y')
        print '\n---Finished test in directory: ' + dir + '\n'

        print '---Writing and copying data...',

        if not os.path.exists(secondaryDir):
            os.makedirs(secondaryDir)

        os.chdir(secondaryDir)
        counter = 0
        exists = os.path.exists(dir[:3] + str(counter))
        while exists:
            counter += 1
            exists = os.path.exists(dir[:3] + str(counter))
        os.makedirs(dir[:3] + str(counter))

        shutil.copy('../clientLog', dir[:3] + str(counter))

        os.chdir(dir[:3] + str(counter))
        subprocess.call('python ' + initDir + '/bin/' + dirs[dir])
        os.chdir(initDir)

        #just to make sure - be sure to run pypy!

        subprocess.call('taskkill /im python.exe /f')

        print 'Done!'
        print '\n===============================\n'

main()

import time
import sys
import threading


numThreads = 5000

if(len(sys.argv) >= 2):
        rewrite = sys.argv[1]
else:
        rewrite = raw_input('Overwrite logs? (Input y/n): ')
if(rewrite in ['y', 'Y']):
        f = open('clientLog', 'w')
else:
        f = open('clientLog', 'a')

print 'Started'
startTime = time.time()
threads = []
for i in range(0,numThreads):
    thing = threading.Thread()
    threads.append(thing)
for thread in threads:
    thread.start() #takes around .68 seconds... chopping off .5 would be pretty nice

totalTime = time.time() - startTime
print 'Finished: ' + str(totalTime)

f.write('1 ' + str(numThreads) + ' ' + str(totalTime) + '\n')

import time
import sys
import Queue

numQueues = 10000

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
for i in range(0,numQueues):
    thing = Queue.Queue()

totalTime = time.time() - startTime
print 'Finished: ' + str(totalTime)

f.write('1 ' + str(numQueues) + ' ' + str(totalTime) + '\n')

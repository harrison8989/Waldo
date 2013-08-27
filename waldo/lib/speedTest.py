import time

start = []
stop = []

numTrials = 1000

def startTime():
    start.append(time.time())

def stopTime(string = 'speedTest'):
    stop.append(time.time())
    getTime(string)

def getTime(string = 'speedTest'):
    if len(start) % numTrials == 0 and len(stop) % numTrials == 0:
        alen = len(start)
        total = []

        for i in range(0,alen / numTrials):
            total.append(0)

        for j in range(0,alen):
            total[j % (alen / numTrials)] -= start[j]
            total[j % (alen / numTrials)] += stop[j]

        print string, total

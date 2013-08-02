import matplotlib.pyplot as plt
import numpy as np
import sys
import random

def plotify():
    '''
    Basic plotter for plotting server data.
    Plots thoroughput and latency.
    Note that only the anaconda python version works. (cuz it has all
    the goodies and stuffz)

    Requires super raw data, where each client is listed out (
    as opposed to aggregated raw data, which lists numbers of
    clients out one by one)

    Takes MULTIPLE FOLDERS as opposed to single files.
    '''
    fileName = 'clientLog'
    colors = ['b','g','r','c','m','y','k']
    marker = ['s','o','^','D']
    style = ['bs','go','r^','cD','m8']
    styleCounter = 0


    folders = []
    if(len(sys.argv) >= 2):
        with open(sys.argv[1]) as dirs:
            for dir in dirs:
                folders.append(dir[0:-1])
    else:
        print 'Please input a file containing the directories.'
        return 0



    for folder in folders:

        f_x = []
        f_y = []
        f_processed = []

        with open(folder + '/' + fileName, 'r') as clientLog:

            for clientData in clientLog:
                cData = clientData.split()

                if cData is not []:

                    datum = int(cData[0]) * float(cData[2]) / (float(cData[1]))
                    if(int(cData[0]) not in f_x):
                        f_x.append(int(cData[0]))
                        f_y.append([datum])
                    else:
                        f_y[f_x.index(int(cData[0]))].append(datum)

        for yList in f_y:
            thing = sum(yList) / len(yList)
            f_processed.append(thing)

        plt.plot(f_x, f_processed, style[styleCounter % len(style)], label=folder)
        styleCounter += 1

    plt.title('Average Latency vs. Number of Clients (seconds/message)')
    plt.xlabel('Number of Clients')
    plt.ylabel('Seconds per message')
    plt.legend(loc='upper left')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('latency.png', dpi=200)
    plt.clf()

    styleCounter = 0

    for folder in folders:

        f_x = []
        f_y = []
        f_processed = []

        with open(folder + '/' + fileName, 'r') as clientLog:

            for clientData in clientLog:
                cData = clientData.split()

                if cData is not []:

                    datum = float(cData[1]) / float(cData[2])
                    if(int(cData[0]) not in f_x):
                        f_x.append(int(cData[0]))
                        f_y.append([datum])
                    else:
                        f_y[f_x.index(int(cData[0]))].append(datum)

        for yList in f_y:
            thing = sum(yList) / len(yList)
            f_processed.append(thing)

        plt.plot(f_x, f_processed, style[styleCounter], label=folder)
        styleCounter += 1

    plt.title('Average Throughput vs. Number of Clients (messages/second)')
    plt.xlabel('Number of Clients')
    plt.ylabel('Messages per second')
    plt.legend(loc='lower left')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('throughput.png', dpi=200)
    plt.clf()


plotify()

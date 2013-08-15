import matplotlib.pyplot as plt
import numpy as np
import sys
import random
import os
from datetime import date

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
    style = ['bs','go','r^','cD','m8','kv']
    styleCounter = 0

    labels = []
    plots = []

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

                if clientData is not []:
                    if clientData[0] == '#':
                        labels.append(clientData[1:])
                    else:
                        labels.append(folder)
                        cData = clientData.split()
                        datum = int(cData[0]) * float(cData[2]) / (float(cData[1]))
                        if(int(cData[0]) not in f_x):
                            f_x.append(int(cData[0]))
                            f_y.append([datum])
                        else:
                            f_y[f_x.index(int(cData[0]))].append(datum)

        for yList in f_y:
            thing = sum(yList) / len(yList)
            f_processed.append(thing)

        plot1, = plt.plot(f_x, f_processed, style[styleCounter % len(style)], label=folder)
        plots.append(plot1)
        styleCounter += 1

    plt.title('Average Latency vs. Number of Clients (seconds/event)')
    plt.xlabel('Number of Clients')
    plt.ylabel('Seconds per event')
    plt.legend(plots, labels, loc='upper left')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('latency.png', dpi=200)
    plt.clf()

    styleCounter = 0
    plots = []

    for folder in folders:

        f_x = []
        f_y = []
        f_processed = []

        with open(folder + '/' + fileName, 'r') as clientLog:

            for clientData in clientLog:

                if clientData is not []:
                    cData = clientData.split()

                    datum = float(cData[1]) / float(cData[2])
                    if(int(cData[0]) not in f_x):
                        f_x.append(int(cData[0]))
                        f_y.append([datum])
                    else:
                        f_y[f_x.index(int(cData[0]))].append(datum)

        for yList in f_y:
            thing = sum(yList) / len(yList)
            f_processed.append(thing)

        plot2, = plt.plot(f_x, f_processed, style[styleCounter], label=folder)
        plots.append(plot2)
        styleCounter += 1

    plt.title('Average Throughput vs. Number of Clients (events/second)')
    plt.xlabel('Number of Clients')
    plt.ylabel('Events per second')
    plt.legend(plots, labels, loc='lower left')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('throughput.png', dpi=200)
    plt.clf()

    with open('legend.txt', 'w') as legend:
        legend.write('Legend for Latency and Throughput Graphs\n')
        legend.write('Created: ' + str(date.today()))
        counter = 0
        for folder in folders:
            initDir = os.getcwd()
            os.chdir(folder)
            try:
                with open('about.txt', 'r') as about:
                    legend.write('\n\n')
                    legend.write(str(counter + 1) + '.)')
                    iterline = iter(about)
                    #if counter > 0:
                    #    next(iterline)
                    for line in iterline:
                        legend.write(line)
                    counter += 1
            except:
                legend.write('No descriptive information was found.')

            os.chdir(initDir)


plotify()

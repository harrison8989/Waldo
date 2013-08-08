import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from datetime import date
import math

def plotify():
    '''
    Basic plotter for plotting server data.
    Plots thoroughput and latency. (OOPS no throughput here!)
    Note that only the anaconda python version works. (cuz it has all
    the goodies and stuffz)

    Requires super raw data, where each client is listed out (
    as opposed to aggregated raw data, which lists numbers of
    clients out one by one)

    Takes MULTIPLE FOLDERS as opposed to single files.
    '''

    fileName = 'clientLog'
    labels = []

    folders = []
    if(len(sys.argv) >= 2):
        with open(sys.argv[1]) as dirs:
            for dir in dirs:
                folders.append(dir[0:-1])
    else:
        print 'Please input a file containing the directories.'
        return 0

    fig, ax = plt.subplots() #should make this common practice

    #generating latency graph
    x = []
    counter = 1
    for folder in folders:

        f_x = []
        f_processed = []

        with open(folder + '/' + fileName, 'r') as clientLog:

            for clientData in clientLog:

                if clientData is not []:

                    if clientData[0] == '#':
                        labels.append(clientData)
                    else:
                        labels.append(counter)
                    counter += 1
                    cData = clientData.split()
                    datum = int(cData[0]) * float(cData[2]) / (float(cData[1]))
                    f_x.append(datum)

        average = sum(f_x) / len(f_x)
        x.append(average)

    xBar = ax.bar(np.arange(len(folders))+.25, x, .50, color = 'r')
    print np.array(folders)
    ax.set_xticks(.50 + np.arange(len(folders)))
    ax.set_xticklabels(labels)

    xShift = .5
    for eks in x:
        log = math.log10(eks)
        plt.text(xShift, 1.05 * eks, round(eks, int(3 - log)),ha='center',va='bottom')
        xShift += 1
    plt.title('Average Per Event Latency')
    plt.xlabel('Trial Number')
    plt.ylabel('Seconds per event')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('latency.png', dpi=200)
    plt.clf()

    with open('legend.txt', 'w') as legend:
        legend.write('Legend for Latency Graph\n')
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
                    if counter > 0:
                        next(iterline)
                    for line in iterline:
                        legend.write(line)
                    counter += 1
            except:
                legend.write('No descriptive information was found.')

            os.chdir(initDir)



plotify()

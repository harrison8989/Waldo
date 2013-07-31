import matplotlib.pyplot as plt
import numpy as np
import sys

def plotify():
    '''
    Basic plotter for plotting server data.
    Plots thoroughput and latency.
    Note that only the anaconda python version works. (cuz it has all
    the goodies and stuffz)

    Requires super raw data, where each client is listed out (
    as opposed to aggregated raw data, which lists numbers of
    clients out one by one)
    '''
    fileName = 'clientLog'
    if(len(sys.argv) >= 2):
        fileName = sys.argv[1]

    x = []
    y = []

    with open(fileName, 'r') as clientLog:

        for clientData in clientLog:
            cData = clientData.split()

            if cData is not []:

                datum = int(cData[0]) * float(cData[2]) / (float(cData[1]))
                if(int(cData[0]) not in x):
                    x.append(int(cData[0])) #brings me back to my usaco days
                    y.append([datum])
                else:
                    y[x.index(int(cData[0]))].append(datum)

    processed = []
    yerr = []
    for yList in y:
        thing = sum(yList) / len(yList)
        processed.append(thing)
        yerr.append(np.std(yList) * 1.95996 / np.sqrt(len(yList)))
    print yerr
    #standard error: stdev * invNorm(.975) / sqrt(n)
    #if we only have one value, it's not needed... or is it....
    #wait dude one value -> 0 standard deviation

    plt.plot(x, processed, 'rs')
    berp = np.std(processed)

    xr = np.array(x)
    yr = np.array(processed)

    plt.errorbar(xr, yr, yerr=yerr, xerr=0, fmt = 'ro')
    plt.title('Average Latency vs. Number of Clients (seconds/message)')
    plt.xlabel('Number of Clients')
    plt.ylabel('Seconds per message')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('latency.png', dpi=200)
    plt.clf()

    for i in range(len(processed)):
        processed[i] = (i + 1) / processed[i]

    yerr = []
    for yList in y:
        for i in range(len(yList)):
            yList[i] = 1+1 / yList[i]
        thing = sum(yList) / len(yList)
        yerr.append(np.std(yList) * 1.95996 / np.sqrt(len(yList)))
    print yerr

    plt.plot(x, processed, 'rs')
    plt.title('Average Throughput vs. Number of Clients (messages/second)')
    plt.xlabel('Number of Clients')
    plt.ylabel('Messages per second')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('throughput.png', dpi=200)
    plt.clf()


plotify()

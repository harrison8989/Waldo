import matplotlib.pyplot as plt
import sys

def plotify():
    '''
    Basic plotter for plotting server data.
    Plots thoroughput and latency.
    Note that only the anaconda python version works. (cuz it has all
    the goodies and stuffz)

    Requires only a "client" file.
    Used if the number of clients doesn't actually increase.
    '''
    fileName = 'clientLog'
    if(len(sys.argv) >= 2):
        fileName = sys.argv[1]

    x = []
    clientY = []

    with open(fileName, 'r') as clientLog:

        for clientData in clientLog:
            cData = clientData.split()

            if cData is not []:
                x.append(cData[0])
                clientY.append(float(cData[2]) / (float(cData[1])))

    plt.plot(x, clientY, 'rs')
    plt.title('Average Latency vs. A Variable (seconds/message)')
    plt.xlabel('Variable')
    plt.ylabel('Seconds per message')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('latency.png', dpi=200)
    plt.clf()

    for i in range(len(clientY)):
        clientY[i] = 1 / clientY[i]

    plt.plot(x, clientY, 'rs')
    plt.title('Average Throughput vs. A Variable (messages/second)')
    plt.xlabel('Variable')
    plt.ylabel('Messages per second')
    plt.gca().set_xlim(left=0)
    plt.gca().set_ylim(bottom=0)
    plt.gcf().set_size_inches(8,4)
    plt.savefig('throughput.png', dpi=200)
    plt.clf()


plotify()

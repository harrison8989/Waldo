import matplotlib.pyplot as plt

def plotify():
    '''
    Basic plotter for plotting server data.
    Plots thoroughput and latency.
    Note that only the anaconda python version works. (cuz it has all
    the goodies and stuffz)

    Requires a "clientLog" file and a "serverLog" file present in the
    current directory.
    '''
    x = []
    clientY = []
    serverY = []

    with open('clientLog', 'r') as clientLog:
        with open('serverLog', 'r') as serverLog:

            for clientData in clientLog:
                serverData = serverLog.readline()
                cData = clientData.split()
                sData = serverData.split()

                if cData is not [] and sData is not []:
                    x.append(cData[0])
                    clientY.append(float(cData[0]) * float(cData[2]) / (float(cData[1])))
                    serverY.append(float(cData[0]) * float(sData[1]) / (float(cData[1])))

    plt.plot(x, clientY, 'ro')
    plt.plot(x, serverY, 'bs')
    plt.title('Average Latency vs. Number of Clients (seconds/message)')
    plt.show()
    plt.clf()

    for i in range(len(clientY)):
        clientY[i] = (i + 1) / clientY[i]

    for i in range(len(serverY)):
        serverY[i] = (i + 1) / serverY[i]

    plt.plot(x, clientY, 'ro')
    plt.plot(x, serverY, 'bs')
    plt.title('Average Throughput vs. Number of Clients (messages/second)')
    plt.show()
    plt.clf()



plotify()

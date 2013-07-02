import matplotlib.pyplot as plt

def main():
    '''
    Basic plotter for plotting server data.
    Note that only the anaconda python version works.

    Requires a "clientLog" file and a "serverLog" file present in the
    current directory. Each line of the above files are assumed to
    have the form

                          num data

    where num is a number and data is a value (such as delay time, ...)
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

                x.append(cData[0])
                clientY.append(cData[1])
                serverY.append(sData[1])

    plt.plot(x, clientY, 'ro')
    plt.plot(x, serverY, 'bs')
    plt.show()


main()

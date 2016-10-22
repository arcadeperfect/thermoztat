from socket import *
import time
import datetime
import json

dataPath = "./jsonBuffer/temp.txt"

address = ('192.168.1.211', 12345)  # Defind who you are talking to (must match arduino IP and port)
client_socket = socket(AF_INET, SOCK_DGRAM)  # Set Up the Socket
client_socket.settimeout(1)  # only wait 1 second for a resonse




while (1):  # Main Loop

    client_socket.sendto("ping", address)
    try:
        rec_data, addr = client_socket.recvfrom(2048)  # Read response from arduino
        #print rec_data + '\n'  # Print the response from Arduino
    except:
        print 'no reply' + '\n'
        rec_data = 'noData'
        pass

    writeData = str(datetime.datetime.now()).split(' ')
    writeData.append(rec_data.split('.')[0])
    print writeData
    '''
    with open('dadata.txt', 'a') as outputFile:
        outputFile.write(str(writeData)+'\n')
    '''

    jsonString = json.dumps(writeData, indent=4)

    print jsonString
    with open(dataPath, 'w') as outfile:
        outfile.write(jsonString)

    time.sleep(3)



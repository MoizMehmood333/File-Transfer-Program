# Reciving files using socket

import os
import socket
import time

#creating the socket
host = input("Host Name: ")
#object for socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#trying to connect to socket
try:
    sock.connect((host,2222))
    print("connected successfully")
except:
    print("unable to connect")
    exit(0)

#reciving the files details from the sender
nameOfTheFile = sock.recv(100).decode()
sizeOfTheFile = sock.recv(100).decode()

# open and write the file, openining it in mode wb "writing in binary"

with open("./incommingFile/" + nameOfTheFile,"wb") as file: 
    c = 0

    #capture the starting and ending time
    #starting time capture

    startTime = time.time()

    #file transfer must take place between these two that is start time and end time
    #running the recv loop untill the file is recivied 
    #reciving the file in small chuncks of data that is 1024 bytes on each iteration
    while c <= int(sizeOfTheFile):
        data = sock.recv(1024)
        if not (data):
            break
        file.write(data)
        c+= len(data)

    #ending the time capture
    endTime = time.time()

print("File Transfer is complete. Total Time consumed in reciving the file : ", endTime-startTime)


#closing the socket
sock.close()
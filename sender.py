#sending files using socket

import os, socket, time
from tracemalloc import start

#creating the socket object

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#trying to connect to socket
try:
    print("connected successfully")
except:
    print("unable to connect")
    exit(0)

# binding the resources
sock.bind((socket.gethostname(),2222))

#number of conncurent users allowed
sock.listen(5)

#print the hostname
print("HOST: ", sock.getsockname())

#Accepting the connection from the client
client, addr = sock.accept()

#getting the file details to be sent

fileName = input("File Name: ")
fileSize = os.path.getsize(fileName)

#Sending file name to the client
#every data that is being sent must be encoded first.

client.send(fileName.encode())
client.send(str(fileSize).encode())

#opening and reafing the file $ rb read in binary

with open(fileName, "rb") as file: 
    c = 0

    #capture the starting and ending time
    #starting time capture

    startTime = time.time()

    #the send function loop will take place between starting and ending time
    #running the loop untill the file has been sent

    while c<= fileSize: 
        data = file.read(1024)
        if not (data):
            break
        client.sendall(data)
        c+= len(data)


    #ending the time capture
    endTime = time.time()

print("File has been sent. Time taken: ",endTime-startTime)

#closing the socket
sock.close()
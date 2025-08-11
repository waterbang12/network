# UDPPingerServer.py 
# We will need the following module to generate randomized lost packets 
import random 
from socket import * 
from time import *
# Create a UDP socket  
# Notice the use of SOCK_DGRAM for UDP packets 
clientSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket 
#clientSocket.sendto('message',('127.0.0.1',12000))
for i in range(10):
    
    try:
# Assign IP address and port number to socket 
        clientSocket.sendto('message'.encode(),('127.0.0.1',12000))
        start=monotonic()
        clientSocket.settimeout(1.0)#1.0s after
        mesg,serverAddress=clientSocket.recvfrom(1024)
        end=monotonic()
        print('mesg:',mesg.decode(),'time:',end-start)
        
    except OSError:
        print('request timed out')
clientSocket.close()

#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverport=1234
serverSocket.bind(('',serverport))
serverSocket.listen(1)

#Fill in end
while True:
 #Establish the connection
 print('Ready tof serve...')
 connectionSocket, addr = serverSocket.accept()#accept handshake and get address(ip주소) of sender, 소켓 열기

 try:
    message =connectionSocket.recv(1024)
    #print(message)
    

    

     #Fill in end
    
    filename = message.split()[1]
    #print(filename)
    if filename == b"/favicon.ico":
      connectionSocket.send(b"HTTP/1.1 204 No Content\r\n\r\n")
      connectionSocket.close()
      continue
    
    #print(filename)
    f = open(filename[1:])
    
    outputdata = f.read()
    #Send one HTTP header line into socket
    #Fill in start
    connectionSocket.send("HTTP/1.1 200 OK\r\n"
            f"Content-Length: {len(outputdata)}\r\n"
            "Content-Type: text/html\r\n"
            "Connection: close\r\n".encode())
    #Fill in end
    #Send the content of the requested file to the client
    
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    
    #print(message)
    connectionSocket.close()
    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data 
    
    #Terminate the program after sending the corresponding data 
 except IOError:
  print('no connection') 
 #Send response message for file not found
 #Fill in start
  connectionSocket.send(
        "HTTP/1.1 404 Not Found\r\n"
        f"Content-Length: {len('404 Not Found\r\n')}\r\n"
        "Content-Type: text/plain\r\n"
        "Connection: close\r\n"
        "\r\n".encode())
  connectionSocket.send("404 Not Found\r\n".encode())
  
 #Fill in end
 #Close client socket
 #Fill in start
  connectionSocket.close()
 #Fill in end
  serverSocket.close()
  sys.exit()#Terminate the program after sending the corresponding data 
  serverSocket.close()
  sys.exit()#Terminate the program after sending the corresponding data 
#import socket module
#import threading

from socket import *
import sys

import threading # In order to terminate the program
import os



serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverport=1234
serverSocket.bind(('',serverport))
serverSocket.listen(1)
#th1=threading.Thread(target=function1)
#th2=threading.Thread(target=)
#Fill in end
script_dir = os.path.dirname(os.path.abspath(__file__))

class Tcp(threading.Thread):
  def __init__(self,connectionSocket,addr):
    super().__init__()
    self.connectionSocket=connectionSocket
    self.addr=addr
    
  def run(self):
    
    print("ready")
    print('thread id:',threading.get_ident(),'addr:',addr) #소켓은 포트 번호 뿐만 아니라 파일 descriptor로 구분, file like 대상임, 같은 포트 번호여도 fd를 커널에서 다르게 assign.


    try:
      message =self.connectionSocket.recv(1024)
      #print(message)
      

      

      #Fill in end
      
      filename = message.split()[1].decode()
      #print(filename)
      if filename == b"/favicon.ico":
        self.connectionSocket.send(b"HTTP/1.1 204 No Content\r\n\r\n")
        self.connectionSocket.close()
        return
      #print(filename[1:])


      script_dir = os.path.dirname(os.path.abspath(__file__))

      filepath = os.path.join(script_dir, filename[1:])

      f = open(filepath)
      #print(f)
      outputdata = f.read()
      print('thread id:',threading.get_ident())
      #Send one HTTP header line into socketz
      #Fill in start
      self.connectionSocket.send("HTTP/1.1 200 OK\r\n"
              f"Content-Length: {len(outputdata)}\r\n"
              "Content-Type: text/html\r\n"
              "Connection: close\r\n".encode())
      #Fill in end
      #Send the content of the requested file to the client
      self.connectionSocket.send(outputdata.encode())
      '''
      for i in range(0, len(outputdata)):
          self.connectionSocket.send(outputdata[i].encode())
          self.connectionSocket.send("\r\n".encode())
      '''
      
      #print(message)
      self.connectionSocket.close()
      print('success')
      return
      #serverSocket.close()
      #sys.exit()#Terminate the program after sending the corresponding data 
      
      #Terminate the program after sending the corresponding data 
    except IOError:
      print('no connection') 
    #Send response message for file not found
    #Fill in start
      self.connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n"
            f"Content-Length: {len('404 Not Found\r\n')}\r\n"
            "Content-Type: text/plain\r\n"
            "Connection: close\r\n"
            "\r\n".encode())
      self.connectionSocket.send("404 Not Found\r\n".encode())

    #Fill in end
    #Close client socket
    #Fill in start
    self.connectionSocket.close()
    return
    #Fill in end
    #serverSocket.close()
    #sys.exit()#Terminate the program after sending the corresponding data 

print('main thread')
while True:
  miniSocket,addr=serverSocket.accept()
  print(miniSocket,addr)
  server=Tcp(miniSocket,addr) #다시 부른다
  server.start()
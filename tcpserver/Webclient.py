#import socket module
import sys
from socket import *
import sys # In order to terminate the program
clientSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverport=1234
serverhost='127.0.0.1'
clientSocket.connect((serverhost,1234))
if len(sys.argv)<2:
    print('insufficient arguments')
else:
    filename=sys.argv[1]



request="GET "+filename+' HTTP/1.1\r\n''Host: '+serverhost+'\r\n''Connection: close\r\n'
'user-agent:python\r\n''Accept-language:eng\r\n'
clientSocket.send(request.encode())
print('here')
data=b""
while(b"\r\n\r\n" not in data):
    chunck=clientSocket.recv(1)
    if not chunck:
        break#예외 처리
    data+=chunck
header=data.decode()
for i in header.split("\r\n"):
    if i.lower().startswith('content-length:'):
        length=i.split(':')[1].strip()
print(length)
actual_data=clientSocket.recv(int(length))
print("Raw bytes:", repr(actual_data))
lang=actual_data.decode()
print("Raw bytes2:", repr(actual_data))

print(actual_data)
print("from server:",header+lang)
print("Raw bytes3:", repr(lang))#hello html is retreived from disk, so takes time unlike 404 which is hardcoded, no data in recv, need looped coding




clientSocket.close()

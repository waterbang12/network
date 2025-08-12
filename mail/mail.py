import base64
from socket import *
import ssl 
import smtplib
import cred

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n" 
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = 'smtp.gmail.com' 
# Create socket called clientSocket and establish a TCP connection with mailserver 
#Fill in start 
USER_naver=cred.USER_naver
PASS_naver=cred.PASS_naver
USER_google=cred.USER_google
PASS_google=cred.PASS_google


context=ssl.create_default_context()

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,587))

print('first:',clientSocket.recv(2048).decode())
clientSocket.send("EHLO gmail.com\r\n".encode())
print('ehlo:',clientSocket.recv(2048).decode())
clientSocket.send("STARTTLS\r\n".encode())#should say rdy to tls
print('starttls:',clientSocket.recv(2048).decode())





wrap=context.wrap_socket(clientSocket, server_hostname=mailserver)
#wrap.connect((mailserver,587))  
#Fill in end 
"""recv = clientSocket.recv(1024).decode() 
print(recv) 
if recv[:3] != '220': 
    print('220 reply not received from server.') """
# Send HELO command and print server response. 
heloCommand = 'EHLO gmail.com\r\n' 
wrap.send(heloCommand.encode()) 
recv1 = wrap.recv(1024).decode() 
print('recv1:',recv1) 
if recv1[:3] != '250': 
    print('250 reply not received from server.') 
# Send MAIL FROM command and print server response. 
# Fill in start 
token = base64.b64encode(("\0".join(["", USER_google, PASS_google])).encode("utf-8")).decode("ascii")
wrap.send(f"AUTH PLAIN {token}\r\n".encode())
print('auth:',wrap.recv(2048).decode())

"""helo='HELO\r\n' 
wrap.send(helo.encode())
recv0=wrap.recv(2048).decode()
print(recv0)
if recv0[:3] != '250': 
    print('250 reply not received from server.') """


mailfromCommand='MAIL FROM:<waterbang12@gmail.com>\r\n'
wrap.send(mailfromCommand.encode())
recv2=wrap.recv(2048).decode()
print('2:',recv2)
if recv2[:3] != '250': 
    print('250 reply not received from server.') 
# Fill in end 
# Send RCPT TO command and print server response. 
rcptCommand='RCPT TO:<waterbang12@naver.com>\r\n'
wrap.send(rcptCommand.encode())
recv3=wrap.recv(2048).decode()
print(recv3)
if recv3[:3] != '250': 
    print('250 reply not received from server.') 

# Send DATA command and print server response.  
DataCommand='DATA\r\n' 
wrap.send(DataCommand.encode())
recv4=wrap.recv(2048).decode()
print(recv4)
if recv4[:3] != '354': 
    print('354 reply not received from server.') 
# Fill in start 
# Fill in end 
# Send message data. 
wrap.send(msg.encode())
wrap.send(endmsg.encode())
recv5=wrap.recv(2048).decode()
print(recv5)
if recv5[:3] != '250': 
    print('250 reply not received from server.') 
# Fill in start 
# Fill in end 
# Message ends with a single period. 
wrap.send('QUIT\r\n'.encode())

recv6=wrap.recv(2048).decode()
print(recv6)
if recv6[:3] != '221': 
    print('221 reply not received from server.') 
# Fill in start 
# Fill in end 
# Send QUIT command and get server response. 
# Fill in start 
# Fill in end 
#the client server or application
from socket import*
serverName='localhost'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
a=input('enter the first number:')
clientSocket.sendto(a.encode(),(serverName,serverPort))

b=input('enter the second number:')
clientSocket.sendto(b.encode(),(serverName,serverPort))
f,serverAddress=clientSocket.recvfrom(2048)
print(f.decode())
clientSocket.close()


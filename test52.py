#the server 
from socket import*
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('the server is ready to receive')
while True:
    a,clientAddress=serverSocket.recvfrom(2048)
    c=int(a.decode())
    b,clientAddress=serverSocket.recvfrom(2048)
    d=int(b.decode())
    f=c*d
    serverSocket.sendto(str(f).encode(),clientAddress)
    
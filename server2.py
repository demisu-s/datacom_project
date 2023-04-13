from socket import *

serverPort = 12000
s = socket(AF_INET, SOCK_DGRAM)
s.connect(('8.8.8.8',80))
hostname = s.getsockname()[0]
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('Join our server!')
print ('IP Address: ' + hostname + '\nPort number: ' + str(serverPort))
print('The server is ready to receive')
isConnected = True
while isConnected:
     connectionSocket, addr = serverSocket.accept()
     clientName = connectionSocket.recv(1024).decode()
     print(clientName)
     clientNum = int(connectionSocket.recv(1024).decode())
     if clientNum > 100 or clientNum < 1:
         print('Server is shutting down...')
         connectionSocket.close()
         isConnected = False
     else:
         name = "Damisu's server"
         num = 13
         sum = num + clientNum
         print ('Server name: ' + name,'\nClient name: ',clientName, '\nServer Number: ', str(num), '\nClient Number: ' , clientNum, '\nSum: ' ,sum)
         connectionSocket.send(name.encode())
         connectionSocket.send(str(num).encode())
         connectionSocket.close()
        
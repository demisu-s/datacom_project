# print ('hello world')
# num = int(input('Enter a number'))
# print (str(num+5))
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
userName = input('Enter your username:')
clientSocket.send(userName.encode())
password = input('Enter your password:')
clientSocket.send(password.encode())
serverMessage = clientSocket.recv(1024)
print (serverMessage.decode())
clientSocket.close()
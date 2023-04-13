from socket import *
serverName = '10.5.206.218'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
name = input("Enter Your Username: ")
clientSocket.send(name.encode())
password = input("Enter Your Password: ")
clientSocket.send(password.encode())
serverMessage = clientSocket.recv(1024)
print(serverMessage.decode())
clientSocket.close()
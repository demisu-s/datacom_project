from socket import *
serverName = input('Enter the IP address: ')
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
name = input("Enter Your Name: ")
clientSocket.send(name.encode())
num = int(input("Enter a number from 1 to 100: "))
clientSocket.send(str(num).encode())
try:
    serverMessage = clientSocket.recv(1024).decode()
    serverResponse = clientSocket.recv(1024).decode()
    serverNum = int(serverResponse)
    sum = num + serverNum
    print('Client name: ', name, '\nServer name: ', serverMessage,
          '\nClient Number: ', num, '\nServer Number: ', serverNum, '\nSum: ', sum)
    clientSocket.close()
except:
    print('Server is down...')
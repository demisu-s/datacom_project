from socket import *
import random
import threading

userName1 = 'Solomon'
userName2 = 'Adam'
password1 = '1234'
password2 = '5678'
def client_thread(connectionSocket, addr):
     messages = ["Opportunities don't happen, you create them.", "I hope your day is as warm as a cup of coffee." , 
            "It's a good day to show the world your talent." ,"Welcome to the land of 13 months of sunshine."]
     clientName = connectionSocket.recv(1024).decode()
     print ('Received from: ' + clientName)
     clientPassword = connectionSocket.recv(1024).decode()
     verified = checkUser(clientName, clientPassword)
     message = "From Damisu's server: " + messages[num]
     if verified:
          connectionSocket.send(message.encode())
     connectionSocket.close()
def checkUser(name, passw):
     if (name == userName1 and passw == password1) or (name==userName2 and passw == password2) :
          return True

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     num = random.randint(0,3)
     connectionSocket, addr = serverSocket.accept()
     new_thread = threading.Thread(target=client_thread,args=(connectionSocket, addr))
     new_thread.start()
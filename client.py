import socket
from socket import *
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1200))
while True:
  msg=s.recv(1024)
  print(msg.decode())

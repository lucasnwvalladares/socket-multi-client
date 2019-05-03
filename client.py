import socket
import thread

def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        print(addr, ' >> ', msg)
        msg = raw_input('SERVER >> ')
        clientsocket.send(msg)
    clientsocket.close()
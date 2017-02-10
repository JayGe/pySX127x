#!/usr/bin/env python3

# used for testing socket_transceiver.py
# connects to socket and allows user to send ascii payload

import socket

pream = bytes(b"\xff\xff\x00\x00")

def sock_client():
        host = '127.0.0.1'
        port = 20000
         
        sock = socket.socket()
        sock.connect((host,port))
         
        message = input('>> ')
         
        while message != 'quit':
                sock.send(bytearray(message,'utf-8'))

                data = bytearray(sock.recv(1024))
                #data = bytearray(sock.recv(1024)).decode('ascii')
                 
                #print ('From LoRa: ' + data)                 
                #print (pream)                 
                #print (data[0:4])                 
                if data[0:4] == pream:
                  print ('From LoRa: ' + data[4:].decode('ascii'))
 
                message = input('>> ')
                 
        sock.close()
 
if __name__ == '__main__':
    sock_client()

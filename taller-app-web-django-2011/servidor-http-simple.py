#!/usr/bin/python

#
# Simple HTTP Server
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2010
# September 2009
#

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTLM page
#  (in a loop)

while True:
    print 'Waiting for connections'
    (recvSocket, address) = mySocket.accept()
    print 'HTTP request received:'
    print recvSocket.recv(1024)
    recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
		    "<html><body><h1>Hello World!</h1></body></html>" +
		    "\r\n")
    recvSocket.close()

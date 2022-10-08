"""Sockets are endpoints of a communication that send
and recieve data that sits on an IP and a Port"""
import socket

# Making the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# af_inet is to tell that it is using ipv4
# sock_stream is there to tell that it will use TCP

# Connect to the sever
s.connect((socket.gethostname(), 1234))
# here we try to connect to the specified address and port

while True:
    # Recieve the data
    msg = s.recv(1024)
    # this specifies the size of data that we want to recieve
    # we will take data in buffers of 8 as it is easy to scale

    # Print the msg
    print(msg.decode("utf-8"))
    # we need to decode the message before printing it
    break

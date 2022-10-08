"""Sockets are endpoints of a communication that send
and recieve data that sits on an IP and a Port"""
import socket


msg = "Welcome to the server"
print(f"{len(msg):<20}"+msg)



""" This is commented out as I worked on something better.
    There is a limit to what is sent over so I am looking out
    for it by adding a header so that it tells me what is
    the length of the message before hand."""

# # Making the socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # af_inet is to tell that it is using ipv4
# # sock_stream is there to tell that it will use TCP
#
#
# # Binding the object
# s.bind((socket.gethostname(),1234))
# # this associates the socket with the ip address,
# # port and address family. Here we set the ip address to our
# # host machine and the port to "1234"
#
# # This limits the queue to just 5 members
# s.listen(5)
#
#
# # Listening for a reply (forever)
#
# while True:
#     clientsocket, address = s.accept()
#     """ clientsocket stores the socket of the
#         client that wants to connect"""
#     """ address stores the address of the client"""
#     print(f'Connection from {address} has been established')
#     clientsocket.send(bytes("Welcome to the server!", "utf-8"))
#     clientsocket.close()

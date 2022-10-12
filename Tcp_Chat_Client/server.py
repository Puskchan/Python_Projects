"""Sockets are endpoints of a communication that send
and recieve data that sits on an IP and a Port"""
import socket
import time
import pickle

HEADERSIZE = 10

# Making the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# af_inet is to tell that it is using ipv4
# sock_stream is there to tell that it will use TCP


# Binding the object
s.bind((socket.gethostname(),1234))
# this associates the socket with the ip address,
# port and address family. Here we set the ip address to our
# host machine and the port to "1234"

# This limits the queue to just 5 members
s.listen(5)

# Listening for a reply (forever)
while True:
    clientsocket, address = s.accept()
    """ clientsocket stores the socket of the
        client that wants to connect"""
    """ address stores the address of the client"""
    print(f'Connection from {address} has been established')

    """ There is a limit to what is sent over so I fixed it
        by adding a header so that it tells me what
        the length of the message is before hand."""

    """ Pickling is the process whereby a Python object hierarchy
        is converted into a byte stream. It is the process of
        serialization/flattening."""
    d = {1:"aditya",2:"hi"}
    msg = pickle.dumps(d)
    # print(msg)

    """ This adds a buffer for the msg length before the actual msg
        I have kept it to a 10 bits number as thats the biggest
        msg I can afford to send."""
    """ Only the header needs to be converted here as the msg is
        already in bytes dur to Pickling."""
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", "utf-8") + msg

    """Sending the data"""
    clientsocket.send(msg)



    # """ This is just a test case to check if I can continously
    #     send data to the client. It sends the current time
    #     to the client every 3 seconds"""
    # while True:
    #     time.sleep(3)
    #     msg = f"The time is: {time.time()}"
    #     msg = f"{len(msg):<{HEADERSIZE}}"+msg
    #     clientsocket.send(bytes(msg, "utf-8"))

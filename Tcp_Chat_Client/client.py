"""Sockets are endpoints of a communication that send
and recieve data that sits on an IP and a Port"""
import socket
import pickle

HEADERSIZE = 10

# Making the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# af_inet is to tell that it is using ipv4
# sock_stream is there to tell that it will use TCP

# Connect to the sever
s.connect((socket.gethostname(), 1234))
# here we try to connect to the specified address and port

while True:
    # As the data incoming is in buffers we need to make the full message
    full_msg = b''
    new_msg = True

    while True:
        # Recieve the data
        msg = s.recv(16)
        # this specifies the size of data that we want to recieve
        # we will take data in buffers of 16 as it is the header size
        # header size will tell us how long the message is


        # Check if the msg is new and print its size
        if new_msg:
            print(f"New message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        # Making the message
        full_msg += msg
        # we need to decode the message before making it

        # Check if the full message is recieved or not
        if len(full_msg)-HEADERSIZE == msglen:
            print("Full msg recieved")
            # Remove the header and return the msg
            print(full_msg[HEADERSIZE:])

            # Here we unpickle the message and printing it
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    # Print the msg
    print(full_msg)

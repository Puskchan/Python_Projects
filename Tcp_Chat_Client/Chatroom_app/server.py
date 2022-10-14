import socket
""" This is for handling multiple connections, it has direct
    interface to the underlying OS implementation. It monitors sockets,
    open files and piped."""
import select


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

""" This will allow us to reconnect to the same address again and again"""
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))

server_socket.listen()

""" This is the list of clients that we have, here we only have one."""
socket_list = [server_socket]

""" Client socket is the key and user data is the value.
    This is to make clients aware of eachother."""
clients = {}

def receive_msg(client_socket):
    """ This is to check if the msg incoming is valid or not.
        And also to get the Data sent by the client."""
    try:
        msg_header = client_socket.recv(HEADER_LENGTH)

        if not len(msg_header):
            return False

        msg_length = int(msg_header.decode("utf=8").strip())
        return {"header" : msg_header, "data" : client_socket.recv(msg_length)}

    except:
        return False

while True:
    """ First is the read list, second is the write list and last (3rd)
        is the list where errors might occur. These are the 3 parameters
        select takes. They are assigned to respective variables."""
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

    """ Go through the read list and it is equal to the server socket then
        accept the connection to that specific client."""
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            """ Receive the client msg on the client socket"""
            user = receive_msg(client_socket)
            if user is False:
                continue

            socket_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new conection from {client_address[0]} : {client_address[1]} username:{user['data'].decode('utf-8')}")
        else:
            message = receive_msg(notified_socket)
            if message is False:
                print(f"Closed connection from {client[notified_socket]['data'].decode('utf-8')}")
                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Receved message from{user['data'].decode('utf-8')} : {message['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + messgage['header'] + message['data'])
    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        del clients[notified_socket]

import socket

ip = "127.0.0.1"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    try:
        # bind() assigns an IP address and a port number to a socket instance
        server.bind((ip, port))
    except:
        print("ERROR")
    print("Server started")

    try:
        # listen() waits for a connection from a client
        server.listen()
    except:
        print("ERROR")

    # connects the client to the server
    # accepts() accepts a connection, receives the clients address and information in a tuple form
    connect, address = server.accept()
    print("New client with address", address)

    while True:

        # receives data from the client
        a = connect.recv(1024)

        print("Client wrote", a.decode())

        # sends a reply to the client
        connect.send(a)
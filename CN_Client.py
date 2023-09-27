import socket

ip = "127.0.0.1"
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    try:
        # connects to the server
        client.connect((ip, port))
        print("Client connected")
    except:
        print("ERROR")

    while True:
        b = input("Say something:")

        # sends data to the server
        client.send(b.encode())

        # receives data from the server
        b = client.recv(1024)

        print("Server replied", b.decode())
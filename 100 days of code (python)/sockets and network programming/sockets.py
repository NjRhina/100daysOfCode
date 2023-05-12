import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(('127.0.0.1', 55555))
s1.listen()

while True:
    client, address = s1.accept()
    print("Connected to{}".format(address))
    client.send("You are connected").encode()
    client.close()

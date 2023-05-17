import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('127.0.0.1', 55555))
message = s1.recv(1024)
s1.close()

print(message.decode())

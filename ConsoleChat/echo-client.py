import socket

HOST = 'localhost'
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello Aibek")
    data = s.recv(1024)

print(f"Recived {data!r}")
import socket

HOST = 'localhost'  # The server's hostname or IP address
PORT = 6050        # The port used by the server
MESSAGE = b"&&A;141;865472034300280;000;000;230119170456;A;-28.683.313;-49.376.476;8;0.9;54;86;76;326781;460|0|27b3|0EA7;27;1;1;1;1;1;0;1;1;1;0;3333;2500;0;1250|470|700;100;100;2b2950;7007b961f;11789068"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(MESSAGE)
    data = s.recv(1024)

print('Received', repr(data))

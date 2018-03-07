# Echo client program
import socket

HOST = 'localhost'  # The remote host

PORT = 50007        # The same port as used by the server

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

so.connect((HOST, PORT))

so.send(' Box')

data = so.recv(1024)

so.close()

print 'Response Received in the clinet : ', repr(data)

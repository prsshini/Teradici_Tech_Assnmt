# Echo server program
import socket

HOST = 'localhost'
PORT = 50007

#function to reverse the string
def reverse_string(data):
    response=data[::-1]
    return ( response )

def mysocket():
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the host and port
    so.bind((HOST, PORT))

#Start to listen
    so.listen(1)

#Connect to the host
    conn, addr = so.accept()
    print 'Connected to', addr
    while 1:
        data = conn.recv(1024)
        print ' Server received the data  : ', data
        if not data:
            break
        response=reverse_string(data)
        print 'String received is reversed: ', response
        conn.send(response)
    conn.close()


if __name__ == '__main__':
    mysocket()

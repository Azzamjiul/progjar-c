import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8000)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    # print >>sys.stderr, 'waiting for a connection'
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()
    # print >>sys.stderr, 'connection from', client_address
    print(sys.stderr, 'connection from ', client_address)
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(200)
        # print >>sys.stderr, 'received "%s"' % data
        print(sys.stderr, 'received ', data)
        if data:
            # print >>sys.stderr, 'sending data back to the client'
            print(sys.stderr, 'sending data back to the client')
            connection.sendall(data)
        else:
            # print >>sys.stderr, 'no more data from', client_address
            print(sys.stderr, 'no more data from', client_address)
        break
    # Clean up the connection
    connection.close()

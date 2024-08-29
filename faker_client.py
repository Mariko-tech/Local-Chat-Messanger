import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = input('Choose fake object(name, address, email or text): ')
    sock.sendall(message.encode())
    sock.settimeout(2)

    try:
        while True:
            data = str(sock.recv(4096).decode())
            if data:
                print('Server response: ' + data)
            else:
                break
    except socket.timeout:
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()
import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/socket_file'
fake = Faker()

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('Starting up on {}'.format(server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    connection, client_address = sock.accept()
    try:
        print('Connection from', client_address)
        while True:
            data = connection.recv(4096)
            if not data:
                print('No data from', client_address)
                break
            data_str = data.decode('utf-8')
            if data_str == "name":
                response = fake.name()
            elif data_str == "address":
                response = fake.address()
            elif data_str == "email":
                response = fake.email()
            elif data_str == "text":
                response = fake.text()
            connection.sendall(response.encode())

    finally:
        print("closing current connection")
        connection.close()
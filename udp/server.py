import socket

def init_server(host: str, port: int):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        data, address = server_socket.recvfrom(1024)
        message = data.decode('utf-8')
        print(message)

if __name__=='__main__':
    HOST = 'localhost'
    PORT = 9000

init_server(HOST, PORT)
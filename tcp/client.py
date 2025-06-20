
import socket

def send_message(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = input("Message: ").encode('utf-8')

    client_socket.connect((host, port))
    client_socket.sendall(message)
    client_socket.close()


if __name__=='__main__':
    HOST = 'localhost'
    PORT = 9000

send_message(HOST, PORT)
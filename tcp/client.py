
import socket

def send_message(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    message = input("Mensagem:")

    client_socket.connect((host, port))
    client_socket.sendall(message.encode('utf-8'))
    client_socket.close()


if __name__=='__main__':
    HOST = 'localhost'
    PORT = 8000

send_message(HOST, PORT)
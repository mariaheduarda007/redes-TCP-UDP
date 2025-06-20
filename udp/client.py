import socket

def send_message(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input('Mensagem: ').encode('utf-8')
    client_socket.sendto(message, (host, port))
    send_message(HOST, PORT)


if __name__=='__main__':

    HOST = 'localhost'
    PORT = 9000

send_message(HOST, PORT)
import socket

def send_message(host: str, port: int):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

<<<<<<< HEAD
    message = input('Mensagem: ').encode('utf-8')
    client_socket.sendto(message, (host, port))
    send_message(HOST, PORT)

=======
    server_socket.sendto(message, (host, port))
>>>>>>> 9572bff0478756b0b61efcc2a37a5688bc512f0d

if __name__=='__main__':

    HOST = 'localhost'
    PORT = 9000

<<<<<<< HEAD
send_message(HOST, PORT)
=======
while True:
    message = input('Mensagem: ').encode('utf-8')
    send_message(HOST, PORT, message)
>>>>>>> 9572bff0478756b0b61efcc2a37a5688bc512f0d

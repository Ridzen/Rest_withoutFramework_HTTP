import socket
import ssl

IP = '192.168.1.108'
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_ssl = ssl.wrap_socket(client, ca_certs="/home/akbar/ssl2/certificate.pem")

client_ssl.connect((IP, PORT))

while True:
    message = input("SII: ")

    if message:
        client_ssl.write(message.encode())
        client.close()


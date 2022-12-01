# Задание для бэкЕнда
# сделать REST сервис
# принимает один запрос POST:{name:'test', time:'14:33 26.11.2022'}
#     name - имя
#     time - время отложенного исполнения
#
# когда наступает время выполнять комманду (print в консоль)
#
# НЕЛЬЗЯ использовать фрэймворки

# Протокол HTTP
#
# HyperText Transfer Protocol (HTTP) — это протокол передачи данных. #
# Изначально для передачи данных в виде гипертекстовых документов в формате HTML,
# сегодня — для передачи произвольных данных.
#
# Этот протокол имеет две особенности, которые должны учитывать все,
# кто работает с этим протоколом: ресурсы и HTTP-глаголы.
#________________________________________________________________________________________________________________________________
# import socket
#
# # def start_my_server():
# from datetime import datetime
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#
# server.bind(('127.0.0.1', 2000))
# server.listen(4)
#
# print('Working ...')
#
# client_socket, address = server.accept()
#
# data = client_socket.recv(1024).decode('utf-8')
# now_date = str(datetime.now().strftime('%H:%M %d.%m.%y'))
# # print(data)
#
# HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html: charset=utf-f\r\n\r\n'
#
# content = 'Well done, Akbar let\' continue...'.encode('utf-8')
#
# client_socket.send(HDRS.encode('utf-8') + content)
#
# print('shutdown this shit ....')


from datetime import date, datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = 'localhost'
PORT = 4444


class TestHHTP(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        decode_body = post_body.decode()
        json_body = json.loads(decode_body)
        self.wfile.write(bytes('{"message": "Успех, Проверь консоль"}', "utf-8"))

        now_date = str(datetime.now().strftime('%H:%M %d.%m.%y'))
        print(now_date)

        if now_date == json_body['time']:
            print("Все работает")
            print(json_body['name'])


server = HTTPServer((HOST, PORT), TestHHTP)
print('Server is running...')

server.serve_forever()
server.server_close()
print('Server was stoped!')

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
# HyperText Transfer Protocol (HTTP)
# ________________________________________________________________________________________________________________________________


from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST_Owner = 'localhost'  # На локальном его открываем
PORT_Owner = 4444  # Порт

# Наша запись выглядит примерно так http://localhost:4444/ сюда мы кидаем наш запрос через PostMan


class TestHHTP(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        c_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(c_len)
        decode_body = post_body.decode()
        json_body = json.loads(decode_body)
        self.wfile.write(bytes('{"message": "Запрос прошел, Проверь консоль"}', "utf-8"))  # Если запрос прошел приходит такое вот сообщение

        now_date = str(datetime.now().strftime('%H:%M %d.%m.%y'))  # Формат time по которую мы задаем, сначала час, минута, день, месяц, год
        print(now_date)

        if now_date == json_body['time']:  # Если формат данных приходит верно, и time совпадает то приходит вот это фраза
            print("Все работает")
            print(json_body['name'])


server = HTTPServer((HOST_Owner, PORT_Owner), TestHHTP)
print('Server is running...')

server.serve_forever()
server.server_close()
print('Server was stoped!')

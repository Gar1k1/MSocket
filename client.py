from Socket import Socket
from threading import Thread
import datetime


class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()

    name = ''

    def set_up(self):
        self.name = input('Input your name: ')
        self.connect(('25.33.98.175', 55000))
        listen_msgs = Thread(target=self.listen_conn)
        listen_msgs.start()

        send_thread = Thread(target=self.send_all, args=(None,))
        send_thread.start()

    def listen_conn(self):
        while True:
            data = self.recv(2048)
            print(data.decode('utf-8'))

    def send_all(self, data):
        while True:
            data = input()
            time = datetime.time
            self.send(f'{self.name}: {data} [{time}]'.encode('utf-8'))


if __name__ == '__main__':
    client = Client()
    client.set_up()

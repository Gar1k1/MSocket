from Socket import Socket
from threading import Thread


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()

    users = []

    def set_up(self):
        self.bind(('25.33.98.175', 55000))
        self.listen(5)
        print('Server started')
        self.listen_conn()

    def listen_msg(self, user, address):
        print(f'\nListen user {user}')
        while True:
            data = user.recv(2048)
            print(f'User {address} sent: ', data.decode('utf-8'))
            self.send_all(data)

    def send_all(self, data):
        for user in self.users:
            user.send(data)

    def listen_conn(self):
        while True:
            print('Waiting for users')
            conn, address = self.accept()
            print(f'Connected {address[0]}:{address[1]}')
            self.users.append(conn)
            ip_address = f'{address[0]}:{address[1]}'
            listen_connected_users = Thread(target=self.listen_msg, args=(conn, ip_address))
            listen_connected_users.start()


if __name__ == '__main__':
    server = Server()
    server.set_up()

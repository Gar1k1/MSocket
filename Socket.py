import socket


class Socket(socket.socket):
    def __init__(self):
        super(Socket, self).__init__(socket.AF_INET, socket.SOCK_STREAM,)

    def server_commands(self):
        raise NotImplementedError

    def set_up(self):
        raise NotImplementedError

    def send_all(self, data):
        raise NotImplementedError

    def listen_msg(self, user, address):
        raise NotImplementedError

    def listen_conn(self):
        raise NotImplementedError

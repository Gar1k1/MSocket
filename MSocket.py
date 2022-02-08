#!/usr/bin/python3
# -*- coding: utf-8 -*-
import keyboard
from Socket import Socket
from threading import Thread
import datetime
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QTextEdit, QLineEdit, QPushButton, QAction
from PyQt5.QtGui import QIcon, QGuiApplication, QActionEvent
from PyQt5 import QtCore, QtGui, QtWidgets

#  Создаём класс сокета наследуя Socket


class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()

    def close_connection(self):
        self.send('Close_conn'.encode('utf-8'))

    def time(self):
            now = datetime.datetime.now()
            time = f'{now.hour}:{now.minute}:{now.second}'
            return time

    name = ''
    stop = False

# Настраиваем подключение к клиенту

    def set_up(self):
        self.connect(('25.33.98.175', 55000))
        listen_msgs = Thread(target=self.listen_conn)
        listen_msgs.start()

# Прослушивание сообщений и вывод их на экран

    def listen_conn(self):
        while True:
            data = self.recv(2048)
            data_send = data.decode('utf-8')
            window.append_msg(data_send)

# Отправка сообщений

    def send_all(self, data):
        self.send(f'{self.name}: {data} [{self.time()}]'.encode('utf-8'))


class Name_window(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self, placeholderText='Enter your name')  # Поле ввода сообщений
        keyboard.add_hotkey('Enter', self.name)
        self.line_edit.move(3, 9)
        self.line_edit.setGeometry(QtCore.QRect(3, 9, 201, 21))
        self.button = QPushButton('OK', self)
        self.button.clicked.connect(self.name)
        self.button.move(210, 7)
        self.setMinimumSize(287, 40)
        self.setMaximumSize(287, 40)
        self.setWindowTitle('MSocket')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

    def name(self):
        name = self.line_edit.text()
        client.name = name
        window.change_name(name)
        self.close()
        window.show()


# Создаём класс окна

class Example(QWidget):
    # Элементы окна
    def __init__(self):
        super().__init__()
        self.name = QLabel('                                               ', self)  # Лебл имени
        self.name.move(10, 10)
        self.name.setStyleSheet("font-family: Segoe UI; font-size: 20px")
        keyboard.add_hotkey('Enter', self.on_click)
        self.text_edit = QTextEdit(self)  # Выдов сообщений
        self.text_edit.move(10, 40)
        self.text_edit.setStyleSheet("font-family: Segoe UI; font-size: 20px")
        self.text_edit.setGeometry(QtCore.QRect(10, 40, 381, 441))
        self.text_edit.setReadOnly(True)
        self.line_edit = QLineEdit(self, placeholderText='Enter your message')  # Поле ввода сообщений
        self.line_edit.setGeometry(QtCore.QRect(10, 490, 281, 20))
        self.button = QPushButton('Send', self)  # Кнопка отправки
        self.button.setGeometry(QtCore.QRect(300, 490, 91, 21))
        self.button.clicked.connect(self.on_click)
        self.setMinimumSize(398, 520)
        self.setMaximumSize(398, 520)
        self.setWindowTitle('MSocket')
        self.setWindowIcon(QtGui.QIcon('icon.png'))

    def closeEvent(self, event):
        event.accept()
        client.close()
        print('Window closed')

    def change_name(self, name):
        self.name.setText(name)

    # Отправка сообщений по нажатию на кнопку

    def on_click(self):
        if self.line_edit.text():
            client.send_all(self.line_edit.text())
            self.line_edit.clear()

    # Вставка отправленных сообщений в экран

    def append_msg(self, text):
        self.text_edit.append(str(text))

# Инициализия всех классов


if __name__ == '__main__':
    import sys
    client = Client()
    client.set_up()
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    window = Example()
    n_w = Name_window()
    sys.exit(app.exec())

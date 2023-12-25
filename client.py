from UI.main import UIMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QThread, pyqtSignal
import sys
import socket  # Network Communications & Data Transmission


class TCPClient(QThread):
    """
    Network Communication and Data Transmission
    """
    display_signal = pyqtSignal(str)

    def __init__(self, data_list):
        super().__init__()
        self.data_list = data_list

    @staticmethod
    def connect_server():
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
        client_socket.connect((host, port))  # connect to the server
        return client_socket

    @staticmethod
    def send_message(client_socket, message):
        client_socket.send(message.encode('utf-8'))

    @staticmethod
    def receive_response(client_socket):
        data = client_socket.recv(1024).decode('utf-8')
        return data

    @staticmethod
    def close_client(client_socket):
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()

    def run(self):
        client_socket = self.connect_server()
        self.send_message(client_socket, self.data_list)
        response = self.receive_response(client_socket)
        self.display_signal.emit(response)


def main():
    app = QApplication(sys.argv)
    interface = UIMainWindow()
    interface.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

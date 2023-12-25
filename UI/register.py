from PyQt5 import QtCore, QtGui, QtWidgets  # Build a graphical interface
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox  # Display graphical interface


class RegisterInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FIFASystem):
        FIFASystem.setObjectName("FIFASystem")
        FIFASystem.resize(720, 634)  # Interface size settings
        FIFASystem.setMaximumSize(720, 634)
        FIFASystem.setMinimumSize(720, 634)
        FIFASystem.setStyleSheet("QWidget#FIFASystem{\n"
                                 "border-image: url(:GUI Project/Register Image.png);\n"
                                 "}")  # Background image settings
        
        # Setting of username label style
        self.username_label = QtWidgets.QLabel(FIFASystem)
        self.username_label.setGeometry(QtCore.QRect(0, 0, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(20)
        font.setItalic(False)
        self.username_label.setFont(font)
        self.username_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.username_label.setScaledContents(False)
        self.username_label.setObjectName("username_label")
        
        # Setting of password label style
        self.password_label = QtWidgets.QLabel(FIFASystem)
        self.password_label.setGeometry(QtCore.QRect(0, 140, 121, 141))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(20)
        font.setItalic(False)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label.setScaledContents(False)
        self.password_label.setObjectName("password_label")
        
        # Setting of username line style
        self.username_line = QtWidgets.QLineEdit(FIFASystem)
        self.username_line.setGeometry(QtCore.QRect(200, 60, 331, 31))
        self.username_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.3);")
        self.username_line.setObjectName("username_line")
        
        # Setting of password line style
        self.password_line = QtWidgets.QLineEdit(FIFASystem)
        self.password_line.setGeometry(QtCore.QRect(200, 200, 331, 31))
        self.password_line.setStyleSheet("background-color: rgb(255, 255, 255, 0.3);")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        
        # Setting of confirm password line style
        self.password_line_2 = QtWidgets.QLineEdit(FIFASystem)
        self.password_line_2.setGeometry(QtCore.QRect(200, 340, 331, 31))
        self.password_line_2.setStyleSheet("background-color: rgb(255, 255, 255, 0.3)")
        self.password_line_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_2.setObjectName("password_line_2")
        
        # Setting of confirm password label style
        self.password_label_2 = QtWidgets.QLabel(FIFASystem)
        self.password_label_2.setGeometry(QtCore.QRect(0, 280, 121, 151))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(20)
        font.setItalic(False)
        self.password_label_2.setFont(font)
        self.password_label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.password_label_2.setScaledContents(False)
        self.password_label_2.setObjectName("password_label_2")
        
        # Setting of registration button style
        self.register_button = QtWidgets.QPushButton(FIFASystem)
        self.register_button.setGeometry(QtCore.QRect(70, 520, 131, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.register_button.setFont(font)
        self.register_button.setObjectName("register_button")
        self.register_button.clicked.connect(self.after_register)  # Signals for completing registration
        
        # Setting of return button style
        self.return_button = QtWidgets.QPushButton(FIFASystem)
        self.return_button.setGeometry(QtCore.QRect(500, 520, 131, 29))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.return_button.setFont(font)
        self.return_button.setObjectName("return_button")
        self.return_button.clicked.connect(self.close)
        self.return_button.clicked.connect(self.main_interface)  # Signal for jumping to the main screen
        
        # Setting of combo box style
        self.comboBox = QtWidgets.QComboBox(FIFASystem)
        self.comboBox.setGeometry(QtCore.QRect(420, 430, 111, 21))
        self.comboBox.setWhatsThis("")
        self.comboBox.setAccessibleName("")
        self.comboBox.setAccessibleDescription("")
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setEditable(False)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtCurrent)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.text(FIFASystem)
        QtCore.QMetaObject.connectSlotsByName(FIFASystem)

    def text(self, FIFASystem):
        """
        Set interface element text information
        """
        _translate = QtCore.QCoreApplication.translate
        FIFASystem.setWindowTitle(_translate("FIFASystem", "FIFA World Cup System"))
        self.username_label.setText(_translate("FIFASystem", "Username:"))
        self.password_label.setText(_translate("FIFASystem", "Password:"))
        self.password_label_2.setText(_translate("FIFASystem", "Confirm\n"
                                                               "Password:"))
        self.register_button.setText(_translate("FIFASystem", "Register"))
        self.return_button.setText(_translate("FIFASystem", "Return"))

        self.comboBox.setCurrentText(_translate("FIFASystem", "User"))
        self.comboBox.setItemText(0, _translate("FIFASystem", "User"))
        self.comboBox.setItemText(1, _translate("FIFASystem", "Administrator"))

    def main_interface(self):
        """
        Slot function for jumping to the main screen
        """
        from UI.main import UIMainWindow
        self.main_interface = UIMainWindow()
        self.main_interface.show()

    def after_register(self):
        """
        Slot function for completing registration
        """
        if self.username_line.text().strip() == '' or self.password_line.text().strip() == '' \
                or self.password_line_2.text().strip() == '':
            try:
                QMessageBox.information(self, 'Error', 'Invalid input, please try again.')
            except Exception as error:
                print('Input error %s' % error)
        elif len(self.password_line.text()) < 6:
            QMessageBox.information(self, 'Warning', 'The length of your password is less than 6.')
        elif self.password_line.text() != self.password_line_2.text():
            try:
                QMessageBox.information(self, 'Error', 'The passwords of input are not the same.')
            except Exception as error:
                print('Unknown error %s' % error)
        else:
            username = self.username_line.text().strip()
            password = self.password_line.text().strip()
            user_type = self.comboBox.currentText().strip()

            data_list = f'r {username} {password} {user_type}'
            from client import TCPClient

            self.registration_thread = TCPClient(data_list)
            self.registration_thread.display_signal.connect(self.registration_response)
            self.registration_thread.start()

    def registration_response(self, response):
        response = response.split(' ')
        if response[0] == 'False':
            """
            If the server cannot receive the message, then it will return a list like 'False error message'
            """
            try:
                message = ''
                for word in range(1, len(response)):
                    message += response[word] + ' '
                QMessageBox.information(self, 'Error', message)
            except Exception as error:
                print('Error %s' % error)
        else:
            try:
                reply = QMessageBox.question(self, 'Return', 'Successful Registration. Really return?',
                                             QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                             QMessageBox.Cancel)
            except Exception as error:
                print('Database error %s' % error)
            else:
                if reply == QMessageBox.Yes:
                    self.close()
                    from UI.main import UIMainWindow
                    self.main_interface = UIMainWindow()
                    self.main_interface.show()
                else:
                    pass


import UI.Image as Image  # Load image

if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = RegisterInterface()
    interface.show()
    sys.exit(app.exec_())

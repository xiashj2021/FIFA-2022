import re
import sys
from PyQt5 import QtCore, QtGui  # Build a graphical interface
# Display graphical interface
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton, QApplication, QMainWindow, QMessageBox

class AdministratorInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FIFASystem):
        FIFASystem.setObjectName("FIFASystem")
        FIFASystem.resize(1122, 734)  # Interface size settings
        FIFASystem.setMaximumSize(1122, 734)
        FIFASystem.setMinimumSize(1122, 734)
        FIFASystem.setStyleSheet("QWidget#FIFASystem{\n"
                                 "border-image: url(:GUI Project/Administrator Image.png);\n"
                                 "}")  # Background image settings

        self.date_line = self.createLineEdit(FIFASystem, 220, 200, 331, 31)
        self.teamname_label = self.createLabel(FIFASystem, 10, 20, 121, 151, "Vladimir Script", 20, "Teamname:")
        self.racetype_line = self.createLineEdit(FIFASystem, 780, 200, 331, 31)
        self.time_line = self.createLineEdit(FIFASystem, 780, 80, 331, 31)
        self.score_label = self.createLabel(FIFASystem, 10, 260, 121, 151, "Vladimir Script", 20, "Score:")
        self.racetype_label = self.createLabel(FIFASystem, 630, 140, 121, 151, "Vladimir Script", 20, "Race Type:")
        self.score_line = self.createLineEdit(FIFASystem, 220, 320, 331, 31)
        self.time_label = self.createLabel(FIFASystem, 630, 20, 121, 151, "Vladimir Script", 20, "Time:")
        self.date_label = self.createLabel(FIFASystem, 10, 140, 121, 151, "Vladimir Script", 20, "Date:")
        self.teamname_line = self.createLineEdit(FIFASystem, 220, 80, 331, 31)
        self.event_label = self.createLabel(FIFASystem, 630, 260, 121, 151, "Vladimir Script", 20, "Event:")
        self.event_line = self.createLineEdit(FIFASystem, 780, 320, 331, 31)
        self.status_line = self.createLineEdit(FIFASystem, 220, 430, 331, 31)
        self.status_label = self.createLabel(FIFASystem, 10, 370, 121, 151, "Vladimir Script", 20, "Status:")
        
        self.returnButton = self.createButton(FIFASystem, 990, 430, 121, 31, "Times New Roman", 12, "Return")
        self.returnButton.clicked.connect(self.close)
        self.returnButton.clicked.connect(self.main_interface)  # Signal for jumping to the main screen
        
        self.insertButton = self.createButton(FIFASystem, 990, 500, 121, 31, "Times New Roman", 12, "Insert")
        self.insertButton.clicked.connect(self.after_insert)  # Signal for completing insert
        
        self.updateButton = self.createButton(FIFASystem, 990, 570, 121, 31, "Times New Roman", 12, "Update")
        self.updateButton.clicked.connect(self.after_update)  # Signal for completing upgrade

        self.text(FIFASystem)
        QtCore.QMetaObject.connectSlotsByName(FIFASystem)

    def createLineEdit(self, parent, x, y, width, height):
        line_edit = QLineEdit(parent)
        line_edit.setGeometry(QtCore.QRect(x, y, width, height))
        line_edit.setStyleSheet("background-color: rgb(255, 255, 255, 0.5);")
        return line_edit

    def createLabel(self, parent, x, y, width, height, font_family, font_size, text):
        label = QLabel(parent)
        label.setGeometry(QtCore.QRect(x, y, width, height))
        font = QtGui.QFont()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        font.setItalic(False)
        label.setFont(font)
        label.setStyleSheet("color: rgb(255, 255, 255);")
        label.setScaledContents(False)
        label.setText(text)
        return label

    def createButton(self, parent, x, y, width, height, font_family, font_size, text):
        button = QPushButton(parent)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        font = QtGui.QFont()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        button.setFont(font)
        button.setObjectName(text + "Button")
        return button

    def text(self, FIFASystem):
        _translate = QtCore.QCoreApplication.translate
        FIFASystem.setWindowTitle(_translate("FIFASystem", "FIFA World Cup System"))
        self.teamname_label.setText(_translate("FIFASystem", "Teamname:"))
        self.score_label.setText(_translate("FIFASystem", "Score:"))
        self.racetype_label.setText(_translate("FIFASystem", "Race Type:"))
        self.time_label.setText(_translate("FIFASystem", "Time:"))
        self.date_label.setText(_translate("FIFASystem", "Date:"))
        self.event_label.setText(_translate("FIFASystem", "Event:"))
        self.status_label.setText(_translate("FIFASystem", "Status:"))
        self.returnButton.setText(_translate("FIFASystem", "Return"))
        self.insertButton.setText(_translate("FIFASystem", "Insert"))
        self.updateButton.setText(_translate("FIFASystem", "Update"))

    def main_interface(self):
        """
        Slot function for jumping to the main screen
        """
        from UI.main import UIMainWindow
        self.main_interface = UIMainWindow()
        self.main_interface.show()

    def after_insert(self):
        team_name = self.teamname_line.text().strip()
        race_type_input = self.racetype_line.text()
        score = self.score_line.text().strip()
        date_input = self.date_line.text()
        race_time_input = self.time_line.text()
        event = self.event_line.text().strip()
        status_input = self.status_line.text()

        date_regex = re.compile(r'^(.\D+)*(\d{1,2} [A-Z][a-z]{2} [0-9]{4})+(.+)*$')
        time_regex = re.compile(r'^(.\D+)*(\d{2}:\d{2})+(.+)*$')
        race_type_regex = re.compile(
            r'^(.\d+)*(Group [A-H]|Round of 16|Quarter-final|Semi-final|Play-off for third place|Final)(.+)*$')
        status_regex = re.compile(r'FT|HT|I|A|ET|NS')

        date_data = re.search(date_regex, date_input)
        race_time_data = re.search(time_regex, race_time_input)
        race_type_data = re.search(race_type_regex, race_type_input)
        status_data = re.search(status_regex, status_input)

        if (date_data is None) or (race_type_data is None) or (race_time_data is None) or (status_data is None):
            try:
                QMessageBox.information(
                    self, 'Error', 'Invalid input, please input correct format information you want to insert.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            date = date_data.group(2)
            race_time = race_time_data.group(2)
            race_type = race_type_data.group(2)
            status = status_data.group()
            data_list = f'i_{team_name}_{race_type}_{score}_{date}_{race_time}_{event}_{status}'

            from client import TCPClient
            self.insert_thread = TCPClient(data_list)
            self.insert_thread.display_signal.connect(self.insert_response)
            self.insert_thread.start()

    def insert_response(self, response):
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
                QMessageBox.information(self, 'Insertion', 'Successful Insertion.')
            except Exception as error:
                print('Error %s' % error)

    def after_update(self):
        team_name_input = self.teamname_line.text()
        race_type_input = self.racetype_line.text()
        score_input = self.score_line.text()
        date_input = self.date_line.text()
        race_time_input = self.time_line.text()
        event = self.event_line.text().strip()
        status_input = self.status_line.text()

        date_regex = re.compile(r'^(.\D+)*(\d{1,2} [A-Z][a-z]{2} [0-9]{4})+(.+)*$')
        time_regex = re.compile(r'^(.\D+)*(\d{2}:\d{2})+(.+)*$')
        team_name_regex = re.compile(r'(.\d+)*([A-Z][a-z]+( [A-Z][a-z]+)* vs [A-Z][a-z]+( [A-Z][a-z]+)*)+(.+)*$')
        score_regex = re.compile(r'^(.\D+)*(\d · \d( [(]\d[)] · [(]\d[)])?)+(.+)*$')
        race_type_regex = re.compile(
            r'^(.\d+)*(Group [A-H]|Round of 16|Quarter-final|Semi-final|Play-off for third place|Final)(.+)*$')
        status_regex = re.compile(r'FT|HT|I|A|ET|NS')

        date_data = re.search(date_regex, date_input)
        race_time_data = re.search(time_regex, race_time_input)
        team_name_data = re.search(team_name_regex, team_name_input)
        score_data = re.search(score_regex, score_input)
        race_type_data = re.search(race_type_regex, race_type_input)
        status_data = re.search(status_regex, status_input)

        if (date_data is None) or (race_type_data is None) or (race_time_data is None) or (status_data is None)\
                or (team_name_data is None) or (score_data is None):
            try:
                QMessageBox.information(
                    self, 'Error', 'Invalid input, please input correct format information you want to upgrade.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            date = date_data.group(2)
            race_time = race_time_data.group(2)
            race_type = race_type_data.group(2)
            score = score_data.group(2)
            team_name = team_name_data.group(2)
            status = status_data.group()
            data_list = f'u_{team_name}_{race_type}_{score}_{date}_{race_time}_{event}_{status}'

            from client import TCPClient
            self.update_thread = TCPClient(data_list)
            self.update_thread.display_signal.connect(self.update_response)
            self.update_thread.start()

    def update_response(self, response):
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
                QMessageBox.information(self, 'Insertion', 'Successful Update.')
            except Exception as error:
                print('Error %s' % error)


import UI.Image as Image  # Load image

if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = AdministratorInterface()

    interface.show()
    sys.exit(app.exec_())

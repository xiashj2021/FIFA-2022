import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets  # Build a graphical interface
from PyQt5.QtWidgets import QApplication, QMessageBox  # Display graphical interface
from client import TCPClient


class UserInterface(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, FIFASystem):
        FIFASystem.setObjectName("FIFASystem")
        FIFASystem.resize(1122, 734)
        FIFASystem.setMaximumSize(1122, 734)
        FIFASystem.setMinimumSize(1122, 734)
        FIFASystem.setStyleSheet("QWidget#FIFASystem{\n"
                                 "border-image: url(:GUI Project/User Image.png);\n"
                                 "}")

        self.createButtons(FIFASystem)
        self.createTableWidget(FIFASystem)
        self.createLabelsAndLines(FIFASystem)

        self.text(FIFASystem)
        QtCore.QMetaObject.connectSlotsByName(FIFASystem)

    def createButtons(self, FIFASystem):
        self.queryButton = self.createButton(FIFASystem, "Query", 920, 320)
        self.queryButton.clicked.connect(self.after_query)
        self.returnButton = self.createButton(FIFASystem, "Return", 920, 250)
        self.returnButton.clicked.connect(self.close)
        self.returnButton.clicked.connect(self.main_interface)

    @staticmethod
    def createButton(parent, text, x, y):
        button = QtWidgets.QPushButton(parent)
        button.setGeometry(QtCore.QRect(x, y, 121, 31))
        button.setFont(QtGui.QFont("Times New Roman", 12, QtGui.QFont.Bold, True))
        button.setText(text)
        return button

    def createTableWidget(self, FIFASystem):
        self.tableWidget = QtWidgets.QTableWidget(FIFASystem)
        self.tableWidget.setGeometry(QtCore.QRect(-5, 470, 1131, 271))
        self.tableWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(25)

        for i in range(25):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)

        for i in range(7):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(i, item)

        for row in range(3):
            for col in range(3):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(158)
        self.tableWidget.verticalHeader().setVisible(False)

    def createLabelsAndLines(self, FIFASystem):
        font = QtGui.QFont("Vladimir Script", 20)
        font.setItalic(False)

        self.teamname_label = self.createLabel(FIFASystem, "", 0, 0, font)
        self.teamname_line = self.createLineEdit(FIFASystem, 210, 60)
        self.date_label = self.createLabel(FIFASystem, "", 0, 120, font)
        self.date_line = self.createLineEdit(FIFASystem, 210, 180)
        self.score_label = self.createLabel(FIFASystem, "", 0, 240, font)
        self.score_line = self.createLineEdit(FIFASystem, 210, 300)
        self.racetype_label = self.createLabel(FIFASystem, "", 620, 120, font)
        self.racetype_line = self.createLineEdit(FIFASystem, 770, 180)
        self.time_label = self.createLabel(FIFASystem, "", 620, 0, font)
        self.time_line = self.createLineEdit(FIFASystem, 770, 60)

    @staticmethod
    def createLabel(parent, text, x, y, font):
        label = QtWidgets.QLabel(parent)
        label.setGeometry(QtCore.QRect(x, y, 121, 151))
        label.setFont(font)
        label.setStyleSheet("color: rgb(255, 255, 255);")
        label.setText(text)
        label.setScaledContents(False)
        return label

    @staticmethod
    def createLineEdit(parent, x, y):
        lineEdit = QtWidgets.QLineEdit(parent)
        lineEdit.setGeometry(QtCore.QRect(x, y, 331, 31))
        lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
        return lineEdit

    def text(self, FIFASystem):
        _translate = QtCore.QCoreApplication.translate
        FIFASystem.setWindowTitle(_translate("FIFASystem", "FIFA World Cup System"))
        self.queryButton.setText(_translate("FIFASystem", "Query"))
        self.returnButton.setText(_translate("FIFASystem", "Return"))

        vertical_header_labels = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25"
        ]

        for index, label in enumerate(vertical_header_labels):
            item = self.tableWidget.verticalHeaderItem(index)
            item.setText(_translate("FIFASystem", label))

        horizontal_header_labels = [
            "Team Name", "Race Type", "Score", "Date", "Time", "Event", "Status"
        ]

        for index, label in enumerate(horizontal_header_labels):
            item = self.tableWidget.horizontalHeaderItem(index)
            item.setText(_translate("FIFASystem", label))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.teamname_label.setText(_translate("FIFASystem", "Teamname:"))
        self.date_label.setText(_translate("FIFASystem", "Date:"))
        self.score_label.setText(_translate("FIFASystem", "Score:"))
        self.racetype_label.setText(_translate("FIFASystem", "Race Type:"))
        self.time_label.setText(_translate("FIFASystem", "Time:"))

    def main_interface(self):
        """
        Slot function for jumping to the main screen
        """
        from UI.main import UIMainWindow
        self.main_interface = UIMainWindow()
        self.main_interface.show()

    def after_query(self):
        """
        Slot function for completing query
        """
        time_regex = re.compile(
            r'^(.\D+)*(\d{2}:\d{2})+(.+)*$')
        score_regex = re.compile(
            r'^(.\D+)*(\d · \d( [(]\d[)] · [(]\d[)])?)+(.+)*$')
        date_regex = re.compile(
            r'^(.\D+)*(\d{1,2} [A-Z][a-z]{2}( [0-9]{4})?)+(.+)*$')
        team_name_regex = re.compile(
            r'^(.\d+)*([A-Z][a-z]+(( [A-Z][a-z]+)* vs [A-Z][a-z]+( [A-Z][a-z]+)*)?)+(.+)*$')
        race_type_regex = re.compile(
            r'^(.\d+)*(Group [A-H]|Round of 16|Quarter-final|Semi-final|Play-off for third place|Final)(.+)*$')

        data_mappings = {
            'team_name': (self.teamname_line.text(), team_name_regex),
            'score': (self.score_line.text(), score_regex),
            'date': (self.date_line.text(), date_regex),
            'time': (self.time_line.text(), time_regex),
            'race_type': (self.racetype_line.text(), race_type_regex)
        }

        query_params = {key: regex.search(data)[2] for key, (data, regex) in data_mappings.items() if regex.search(data)}

        if len(query_params) == 0:
            try:
                QMessageBox.information(self, 'Error', 'Invalid input, please input some information you want to know.')
            except Exception as error:
                print('Input error %s' % error)
        else:
            query_string = f'q|{"*".join(query_params.keys())}|{"*".join(query_params.values())}'
            self.start_query_thread(query_string)
            
    def start_query_thread(self, data_string):
        self.query_thread = TCPClient(data_string)
        self.query_thread.display_signal.connect(self.query_response)
        self.query_thread.start()

    def query_response(self, response):
        response = response.split('|')
        if response[0] == 'False':
            """
            If the server cannot receive the message, then it will return a list like 'False|error message'
            """
            try:
                QMessageBox.information(self, 'Error', response[-1])
            except Exception as error:
                print('Error %s' % error)
        else:
            rows = self.tableWidget.rowCount()
            columns = self.tableWidget.columnCount()
            for row in range(rows):
                for column in range(columns):
                    self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(''))
            data = response[-1]
            data_list = data.split('&')
            x = 0
            for row in data_list:
                row_data = row.split('_')
                y = 0
                for column in row_data:
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(column)))
                    y += 1
                x += 1


import UI.Image as Image  # Load image

if __name__ == '__main__':
    app = QApplication(sys.argv)

    interface = UserInterface()
    interface.show()
    sys.exit(app.exec_())

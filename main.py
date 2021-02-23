import sys
import psycopg2
import connectionDB
import uuid
import hashlib
import os
import datetime

from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QTableWidgetItem, QComboBox
from LoginUI import Ui_Login
# from CreateAccUI import Ui_CreateAcc, CreateAcc
from MainWindowUI import Ui_MainWindow
from PyQt5.QtCore import QDate, QDateTime
from MessageBoxes import QBoxes, InfoBox
from StatusUI import Ui_Status


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.loginbutton.clicked.connect(self.loginfunction)

    def loginfunction(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        try:
            cursor.execute("select get_key_and_salt(%s)", (username,))
            m = cursor.fetchall()
            m = list(m)
            for i in m:
                i = str(i)[2:len(i) - 4]
                if self.check_password(i, password):
                    cursor.execute("SELECT public.login(%s, %s)", (username, i))
                    r = cursor.fetchone()
                    global role
                    role = str(r)[1:2]
                    break

            self.accept()
        except psycopg2.errors.RaiseException:
            m = QBoxes.wrongPass(self)
            con.rollback()

    def check_password(self, hashed_password, user_password):
        h_password, salt = hashed_password.split(':')
        if h_password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest():
            return True

    # def gotocreate(self):
    # createacc = CreateAcc()
    # widget.addWidget(createacc)
    # widget.setCurrentIndex(widget.currentIndex() + 1)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.status_button.clicked.connect(self.open_status)

    def open_status(self):
        dialog = Status(self)
        dialog.exec_()


class Status(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Status, self).__init__(parent)

        self.ui = Ui_Status()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.addRecord)
        self.ui.delete_button.clicked.connect(self.deleteRecord)
        self.printRecords()

    def printRecords(self):
        print("Update")
        cursor.execute("SELECT * FROM status;")
        row = 0
        for tup in cursor:
            col = 0
            self.ui.tableWidget.setRowCount(row + 1)
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(row, col, cellInfo)
                col += 1
            row += 1
            self.ui.tableWidget.resizeColumnsToContents()

    def changeRecord(self):
        print("Changed")

    def addRecord(self):
        nameStatus = self.ui.adding_type.text()
        print("Add")
        if nameStatus != "":
            cursor.execute("INSERT INTO status VALUES (DEFAULT, \'{0}\');".format(nameStatus))
        con.commit()
        self.printRecords()
        self.ui.adding_type.clear()

    def deleteRecord(self):
        nameStatus = self.ui.delete_type.text()
        nameID = self.ui.id_category.text()
        print("Delete")
        if nameID != "":
            cursor.execute(
                "DELETE FROM status WHERE status_id=\'{0}\';".format(nameID))
        elif nameStatus != "":
            cursor.execute("DELETE FROM status WHERE name=\'{0}\';".format(nameStatus))
        con.commit()
        self.printRecords()
    # printRecords(self)


if __name__ == "__main__":
    con = connectionDB.connectionDB()
    if con is not None:
        cursor = con.cursor()
    app = QtWidgets.QApplication(sys.argv)
    global role_id
    login = Login()
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())

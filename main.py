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
# from CreateAccUI import Ui_CreateAcc, CreateAcc
from PyQt5.QtCore import QDate, QDateTime
from MessageBoxes import QBoxes, InfoBox
from pyUI.MainWindowUI import Ui_MainWindow
from pyUI.StatusUI import Ui_Status
from pyUI.LoginUI import Ui_Login
from pyUI.PositionsUI import Ui_Positions
from pyUI.CategoriesUI import Ui_Categories
from pyUI.PropertyUI import Ui_Property
from pyUI.RoomWindowUI import Ui_RoomsWindow


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

        cursor.execute("SELECT * FROM free_rooms()")
        for tup in cursor:
            col = 0
            self.ui.Booking.setRowCount(self.ui.Booking.rowCount() + 1)
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.Booking.setItem(self.ui.Booking.rowCount() - 1, col, cellInfo)
                col += 1
            self.ui.Booking.resizeColumnsToContents()

        self.ui.status_button.clicked.connect(self.open_status)
        self.ui.position_button.clicked.connect(self.open_positions)
        self.ui.categories_button.clicked.connect(self.open_categories)
        self.ui.properties_button.clicked.connect(self.open_properties)
        self.ui.rooms_button.clicked.connect(self.open_rooms)

        self.ui.addGuest_Button.clicked.connect(self.add_guest)
        self.ui.searchButton.clicked.connect(self.find_guest)
        self.ui.addBookingButton.clicked.connect(self.add_booking)

    def add_booking(self):
        nameGuest = self.ui.booking_nameEdit.text()
        lastNameGuest = self.ui.booking_lastnameEdit.text()
        passport = self.ui.booking_passportEdit.text()
        arrDate = self.ui.booking_arrivalDateEdit_2.date().toPyDate()
        depDate = self.ui.booking_departureDateEdit.date().toPyDate()
        room = int(self.ui.Booking.item(self.ui.Booking.currentItem().row(), 0).text())

        cursor.execute("SELECT new_booking(find_guest(%s, %s, %s), %s, %s, %s, %s)",
                       (nameGuest, lastNameGuest, passport, room, arrDate, depDate, datetime.date.today()))
        con.commit()


    def find_guest(self):
        nameGuest = self.ui.search_nameEdit.text()
        lastNameGuest = self.ui.search_lastnameEdit.text()
        passport = self.ui.search_passportEdit.text()

        cursor.execute("SELECT guest_id, first_name, last_name, phone_number, birth_date, passport FROM guest WHERE guest_id = find_guest(%s, %s, %s);",
                       (nameGuest, lastNameGuest, passport))
        for tup in cursor:
            col = 0
            self.ui.searchResultTable.setRowCount(self.ui.searchResultTable.rowCount() + 1)
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.searchResultTable.setItem(self.ui.searchResultTable.rowCount() - 1, col,
                                                  cellInfo)
                col += 1
            self.ui.searchResultTable.resizeColumnsToContents()

    def add_guest(self):
        nameGuest = self.ui.nameEdit.text()
        lastNameGuest = self.ui.lastnameEdit.text()
        telephone = self.ui.phoneEdit.text()
        passport = self.ui.passportEdit.text()
        dateBirth = self.ui.dateofbirthEdit.date().toPyDate()
        namePayer = self.ui.nameEdit_payer.text()
        lnPayer = self.ui.lastnameEdit_payer.text()
        psprtPayer = self.ui.passportEdit_payer.text()

        cursor.execute("SELECT guest_reg(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                       (namePayer, lnPayer, psprtPayer,
                        nameGuest, lastNameGuest, telephone,
                        dateBirth, 1, passport))
        con.commit()
        self.ui.nameEdit.clear()
        self.ui.lastnameEdit.clear()
        self.ui.phoneEdit.clear()
        self.ui.passportEdit.clear()
        self.ui.dateofbirthEdit.clear()
        self.ui.nameEdit_payer.clear()
        self.ui.lastnameEdit_payer.clear()
        self.ui.passportEdit_payer.clear()

    def open_status(self):
        dialog = Status(self)
        dialog.exec_()

    def open_positions(self):
        dialog = Position(self)
        dialog.exec_()

    def open_categories(self):
        dialog = Category(self)
        dialog.exec_()

    def open_properties(self):
        dialog = Property(self)
        dialog.exec_()

    def open_rooms(self):
        dialog = Room(self)
        dialog.exec_()


class Room(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Room, self).__init__(parent)

        self.ui = Ui_RoomsWindow()
        self.ui.setupUi(self)

        self.printRecords()

    def printRecords(self):
        print("Update")
        cursor.execute("SELECT * FROM list_rooms();")
        for tup in cursor:
            col = 0
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, col, cellInfo)
                col += 1
            self.ui.tableWidget.resizeColumnsToContents()


class Property(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Property, self).__init__(parent)

        self.ui = Ui_Property()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.addRecord)
        self.ui.delete_button.clicked.connect(self.deleteRecord)
        self.printRecords()

    def printRecords(self):
        print("Update")
        cursor.execute("SELECT * FROM property;")
        for tup in cursor:
            col = 0
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.tableWidget.setItem(self.ui.tableWidget.rowCount() - 1, col, cellInfo)
                col += 1
            self.ui.tableWidget.resizeColumnsToContents()

    def changeRecord(self):
        print("Changed")

    def addRecord(self):
        nameProp = self.ui.adding_type.text()
        print("Add")
        if nameProp != "":
            cursor.execute("INSERT INTO property VALUES (DEFAULT, \'{0}\');".format(nameProp))
        con.commit()
        self.printRecords()
        self.ui.adding_type.clear()

    def deleteRecord(self):
        nameProp = self.ui.delete_type.text()
        nameID = self.ui.id_property.text()
        print("Delete")
        if nameID != "":
            cursor.execute(
                "DELETE FROM property WHERE property_id=\'{0}\';".format(nameID))
        elif nameProp != "":
            cursor.execute("DELETE FROM property WHERE name=\'{0}\';".format(nameProp))
        con.commit()
        self.printRecords()


class Category(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Category, self).__init__(parent)

        self.ui = Ui_Categories()
        self.ui.setupUi(self)

        self.printRecords()
        self.ui.update_button.clicked.connect(self.printRecords)
        self.ui.add_button.clicked.connect(self.addRecord)
        self.ui.delete_button.clicked.connect(self.deleteRecord)

    def printRecords(self):
        print("Update")
        cursor.execute("SELECT * FROM category;")
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
        positionType = self.ui.adding_type.text()
        desc = self.ui.adding_desc.text()
        print("Add")
        if positionType != "":
            cursor.execute("INSERT INTO category VALUES (DEFAULT, \'{0}\', \'{1}\');".
                           format(positionType, desc))
        con.commit()
        self.printRecords()
        self.ui.adding_type.clear()
        self.ui.adding_desc.clear()

    def deleteRecord(self):
        categoryType = self.ui.delete_type.text()
        categoryID = self.ui.id_category.text()
        print("Delete")
        if categoryID != "":
            cursor.execute("DELETE FROM category WHERE category_id=\'{0}\';".format(categoryID))
        elif categoryType != "":
            cursor.execute("DELETE FROM category WHERE name=\'{0}\';".format(categoryType))
        con.commit(self)
        self.printRecords()


class Position(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Position, self).__init__(parent)

        self.ui = Ui_Positions()
        self.ui.setupUi(self)

        self.printRecords()
        self.ui.update_button.clicked.connect(self.printRecords)
        self.ui.add_button.clicked.connect(self.addRecord)
        self.ui.delete_button.clicked.connect(self.deleteRecord)

    def printRecords(self):
        print("Update")
        cursor.execute("SELECT * FROM position;")
        row = 0
        for tup in cursor:
            col = 0
            self.ui.positions_tableWidget.setRowCount(row + 1)
            for item in tup:
                cellInfo = QTableWidgetItem(str(item))
                cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.ui.positions_tableWidget.setItem(row, col, cellInfo)
                col += 1
            row += 1
            self.ui.positions_tableWidget.resizeColumnsToContents()

    def changeRecord(self):
        print("Changed")

    def addRecord(self):
        positionType = self.ui.position_name.text()
        desc = self.ui.adding_desc.text()
        print("Add")
        if positionType != "":
            cursor.execute("INSERT INTO position VALUES (DEFAULT, \'{0}\', \'{1}\');".
                           format(positionType, desc))
        con.commit()
        self.printRecords()
        self.ui.position_name.clear()
        self.ui.adding_desc.clear()

    def deleteRecord(self):
        positionType = self.ui.delete_type.text()
        positionID = self.ui.id_position.text()
        print("Delete")
        if positionID != "":
            cursor.execute("DELETE FROM position WHERE position_id=\'{0}\';".format(positionID))
        elif positionType != "":
            cursor.execute("DELETE FROM position WHERE name=\'{0}\';".format(positionType))
        con.commit(self)
        self.printRecords()


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

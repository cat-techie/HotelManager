import sys

import psycopg2
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from Views import Categories

Form, Window = uic.loadUiType("Views/Positions.ui")
conn = psycopg2.connect(dbname="HotelDB", user="shapochka", port="5432",
                        password="31657101hd", host="", hostaddr="192.168.56.101")
cursor = conn.cursor()

app = QApplication([])
window = Window()
window.setFixedSize(880, 640)
form = Form()
form.setupUi(window)
window.show()


def printRecords():
    print("Update")
    cursor.execute("SELECT * FROM positions;")
    row = 0
    for tup in cursor:
        col = 0
        form.tableWidget.setRowCount(row + 1)
        for item in tup:
            cellInfo = QTableWidgetItem(str(item))
            cellInfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            form.tableWidget.setItem(row, col, cellInfo)
            col += 1
        row += 1
        form.tableWidget.resizeColumnsToContents()


def changeRecord():
    print("Changed")


def addRecord():
    categoryType = form.adding_type.text()
    desc = form.adding_desc.text()
    print("Add")
    if categoryType != "":
        cursor.execute("INSERT INTO positions VALUES (\'{0}\', \'{1}\', DEFAULT);".
                       format(categoryType, desc))
    conn.commit()
    printRecords()


def deleteRecord():
    categoryType = form.delete_type.text()
    categoryID = form.id_category.text()
    print("Delete")
    if categoryID != "":
        cursor.execute("DELETE FROM positions WHERE id=\'{0}\';".format(categoryID))
    elif categoryType != "":
        cursor.execute("DELETE FROM positions WHERE name=\'{0}\';".format(categoryType))
    conn.commit()
    printRecords()


printRecords()
form.update_button.clicked.connect(printRecords)
form.add_button.clicked.connect(addRecord)
form.delete_button.clicked.connect(deleteRecord)

app.exec_()

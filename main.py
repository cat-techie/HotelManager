import sys
import psycopg2
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.uic.properties import QtGui


class MainWindow(QtWidgets.QMainWindow):
    Form, Window = uic.loadUiType("Views/MainPage.ui")
    conn = psycopg2.connect(dbname="HotelDB", user="cat-techie", port="5432",
                            password="31657101hd", host="", hostaddr="")
    cursor = conn.cursor()

    app = QApplication([])
    window = Window()
    window.setFixedSize(880, 640)
    form = Form()
    form.setupUi(window)
    window.show()

   # def openCategories(self):

    app.exec_()

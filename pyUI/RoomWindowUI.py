# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Hotel\Views\RoomsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RoomsWindow(object):
    def setupUi(self, RoomsWindow):
        RoomsWindow.setObjectName("RoomsWindow")
        RoomsWindow.resize(792, 536)
        self.centralwidget = QtWidgets.QWidget(RoomsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 20, 791, 491))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        #RoomsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RoomsWindow)
        QtCore.QMetaObject.connectSlotsByName(RoomsWindow)

    def retranslateUi(self, RoomsWindow):
        _translate = QtCore.QCoreApplication.translate
        RoomsWindow.setWindowTitle(_translate("RoomsWindow", "Список номеров"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RoomsWindow", "Номер"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RoomsWindow", "Статус"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RoomsWindow", "Категория"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RoomsWindow", "Этаж"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("RoomsWindow", "Свойство"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("RoomsWindow", "Детали"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoomsWindow = QtWidgets.QMainWindow()
    ui = Ui_RoomsWindow()
    ui.setupUi(RoomsWindow)
    RoomsWindow.show()
    sys.exit(app.exec_())

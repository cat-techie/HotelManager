# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Hotel\Views\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.catalog = QtWidgets.QTabWidget(self.centralwidget)
        self.catalog.setGeometry(QtCore.QRect(0, 0, 901, 641))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.catalog.setFont(font)
        self.catalog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.catalog.setMovable(True)
        self.catalog.setObjectName("catalog")
        self.Passengers = QtWidgets.QWidget()
        self.Passengers.setObjectName("Passengers")
        self.passengers_tab = QtWidgets.QTabWidget(self.Passengers)
        self.passengers_tab.setGeometry(QtCore.QRect(0, 0, 891, 611))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passengers_tab.setFont(font)
        self.passengers_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.passengers_tab.setObjectName("passengers_tab")
        self.addPassengers = QtWidgets.QWidget()
        self.addPassengers.setObjectName("addPassengers")
        self.label = QtWidgets.QLabel(self.addPassengers)
        self.label.setGeometry(QtCore.QRect(290, 50, 281, 41))
        self.label.setStyleSheet("font-size: 28px")
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(self.addPassengers)
        self.nameEdit.setGeometry(QtCore.QRect(300, 160, 211, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.lastnameEdit = QtWidgets.QLineEdit(self.addPassengers)
        self.lastnameEdit.setGeometry(QtCore.QRect(300, 200, 211, 22))
        self.lastnameEdit.setObjectName("lastnameEdit")
        self.phoneEdit = QtWidgets.QLineEdit(self.addPassengers)
        self.phoneEdit.setGeometry(QtCore.QRect(300, 240, 211, 22))
        self.phoneEdit.setObjectName("phoneEdit")
        self.passportEdit = QtWidgets.QLineEdit(self.addPassengers)
        self.passportEdit.setGeometry(QtCore.QRect(300, 280, 211, 22))
        self.passportEdit.setObjectName("passportEdit")
        self.dateofbirthEdit = QtWidgets.QDateEdit(self.addPassengers)
        self.dateofbirthEdit.setGeometry(QtCore.QRect(300, 320, 211, 21))
        self.dateofbirthEdit.setDate(QtCore.QDate(1900, 1, 1))
        self.dateofbirthEdit.setObjectName("dateofbirthEdit")
        self.addGuest_Button = QtWidgets.QPushButton(self.addPassengers)
        self.addGuest_Button.setGeometry(QtCore.QRect(350, 370, 111, 28))
        self.addGuest_Button.setObjectName("addGuest_Button")
        self.nameEdit_payer = QtWidgets.QLineEdit(self.addPassengers)
        self.nameEdit_payer.setGeometry(QtCore.QRect(530, 160, 211, 22))
        self.nameEdit_payer.setObjectName("nameEdit_payer")
        self.lastnameEdit_payer = QtWidgets.QLineEdit(self.addPassengers)
        self.lastnameEdit_payer.setGeometry(QtCore.QRect(530, 200, 211, 22))
        self.lastnameEdit_payer.setObjectName("lastnameEdit_payer")
        self.passportEdit_payer = QtWidgets.QLineEdit(self.addPassengers)
        self.passportEdit_payer.setGeometry(QtCore.QRect(530, 240, 211, 22))
        self.passportEdit_payer.setObjectName("passportEdit_payer")
        self.passengers_tab.addTab(self.addPassengers, "")
        self.searchPassengers = QtWidgets.QWidget()
        self.searchPassengers.setObjectName("searchPassengers")
        self.label_2 = QtWidgets.QLabel(self.searchPassengers)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 241, 51))
        self.label_2.setStyleSheet("font-size: 28px")
        self.label_2.setObjectName("label_2")
        self.search_nameEdit = QtWidgets.QLineEdit(self.searchPassengers)
        self.search_nameEdit.setGeometry(QtCore.QRect(40, 100, 221, 22))
        self.search_nameEdit.setObjectName("search_nameEdit")
        self.search_lastnameEdit = QtWidgets.QLineEdit(self.searchPassengers)
        self.search_lastnameEdit.setGeometry(QtCore.QRect(290, 100, 221, 22))
        self.search_lastnameEdit.setReadOnly(False)
        self.search_lastnameEdit.setObjectName("search_lastnameEdit")
        self.search_passportEdit = QtWidgets.QLineEdit(self.searchPassengers)
        self.search_passportEdit.setGeometry(QtCore.QRect(530, 100, 221, 22))
        self.search_passportEdit.setObjectName("search_passportEdit")
        self.searchButton = QtWidgets.QPushButton(self.searchPassengers)
        self.searchButton.setGeometry(QtCore.QRect(40, 140, 93, 28))
        self.searchButton.setObjectName("searchButton")
        self.searchResultTable = QtWidgets.QTableWidget(self.searchPassengers)
        self.searchResultTable.setGeometry(QtCore.QRect(40, 190, 611, 191))
        self.searchResultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.searchResultTable.setRowCount(1)
        self.searchResultTable.setColumnCount(6)
        self.searchResultTable.setObjectName("searchResultTable")
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchResultTable.setHorizontalHeaderItem(5, item)
        self.searchResultTable.verticalHeader().setVisible(False)
        self.searchResultTable.verticalHeader().setHighlightSections(True)
        self.passengers_tab.addTab(self.searchPassengers, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.guest_cards = QtWidgets.QTableWidget(self.tab_2)
        self.guest_cards.setGeometry(QtCore.QRect(130, 80, 611, 431))
        self.guest_cards.setObjectName("guest_cards")
        self.guest_cards.setColumnCount(6)
        self.guest_cards.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.guest_cards.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.guest_cards.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.guest_cards.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.guest_cards.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.guest_cards.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.guest_cards.setHorizontalHeaderItem(5, item)
        self.guest_cards.verticalHeader().setVisible(False)
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(360, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.passengers_tab.addTab(self.tab_2, "")
        self.catalog.addTab(self.Passengers, "")
        self.rooms = QtWidgets.QWidget()
        self.rooms.setObjectName("rooms")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.rooms)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 891, 611))
        self.tabWidget_3.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.room_tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.room_tableWidget.setGeometry(QtCore.QRect(40, 60, 771, 541))
        self.room_tableWidget.setObjectName("room_tableWidget")
        self.room_tableWidget.setColumnCount(6)
        self.room_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.room_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.room_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.room_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.room_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.room_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.room_tableWidget.setHorizontalHeaderItem(5, item)
        self.room_tableWidget.horizontalHeader().setVisible(False)
        self.room_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.room_tableWidget.horizontalHeader().setHighlightSections(True)
        self.room_tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.room_tableWidget.verticalHeader().setVisible(False)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(370, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.catalog.addTab(self.rooms, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 0, 871, 611))
        self.tabWidget_2.setAutoFillBackground(False)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.booking_departureDateEdit = QtWidgets.QDateEdit(self.tab_6)
        self.booking_departureDateEdit.setGeometry(QtCore.QRect(260, 450, 211, 22))
        self.booking_departureDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.booking_departureDateEdit.setObjectName("booking_departureDateEdit")
        self.label_30 = QtWidgets.QLabel(self.tab_6)
        self.label_30.setGeometry(QtCore.QRect(310, 20, 251, 41))
        self.label_30.setStyleSheet("font-size: 28px")
        self.label_30.setObjectName("label_30")
        self.addBookingButton = QtWidgets.QPushButton(self.tab_6)
        self.addBookingButton.setGeometry(QtCore.QRect(560, 420, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.addBookingButton.setFont(font)
        self.addBookingButton.setObjectName("addBookingButton")
        self.booking_arrivalDateEdit_2 = QtWidgets.QDateEdit(self.tab_6)
        self.booking_arrivalDateEdit_2.setGeometry(QtCore.QRect(260, 420, 211, 22))
        self.booking_arrivalDateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.booking_arrivalDateEdit_2.setObjectName("booking_arrivalDateEdit_2")
        self.Booking = QtWidgets.QTableWidget(self.tab_6)
        self.Booking.setGeometry(QtCore.QRect(20, 80, 821, 321))
        self.Booking.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Booking.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Booking.setGridStyle(QtCore.Qt.SolidLine)
        self.Booking.setObjectName("Booking")
        self.Booking.setColumnCount(6)
        self.Booking.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Booking.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booking.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booking.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booking.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booking.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Booking.setHorizontalHeaderItem(5, item)
        self.Booking.verticalHeader().setVisible(False)
        self.guest_card_edit_book = QtWidgets.QLineEdit(self.tab_6)
        self.guest_card_edit_book.setGeometry(QtCore.QRect(20, 420, 161, 51))
        self.guest_card_edit_book.setObjectName("guest_card_edit_book")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.booking_arrivalDateEdit = QtWidgets.QDateEdit(self.tab_7)
        self.booking_arrivalDateEdit.setGeometry(QtCore.QRect(280, 100, 211, 22))
        self.booking_arrivalDateEdit.setObjectName("booking_arrivalDateEdit")
        self.booking_room_search = QtWidgets.QComboBox(self.tab_7)
        self.booking_room_search.setGeometry(QtCore.QRect(40, 100, 211, 22))
        self.booking_room_search.setObjectName("booking_room_search")
        self.searchBookingsButton = QtWidgets.QPushButton(self.tab_7)
        self.searchBookingsButton.setGeometry(QtCore.QRect(40, 140, 93, 28))
        self.searchBookingsButton.setObjectName("searchBookingsButton")
        self.searchBookinsResultTable = QtWidgets.QTableWidget(self.tab_7)
        self.searchBookinsResultTable.setGeometry(QtCore.QRect(0, 190, 831, 191))
        self.searchBookinsResultTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.searchBookinsResultTable.setRowCount(1)
        self.searchBookinsResultTable.setColumnCount(8)
        self.searchBookinsResultTable.setObjectName("searchBookinsResultTable")
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.searchBookinsResultTable.setHorizontalHeaderItem(7, item)
        self.searchBookinsResultTable.verticalHeader().setVisible(False)
        self.searchBookinsResultTable.verticalHeader().setHighlightSections(True)
        self.label_13 = QtWidgets.QLabel(self.tab_7)
        self.label_13.setGeometry(QtCore.QRect(40, 30, 241, 51))
        self.label_13.setStyleSheet("font-size: 28px")
        self.label_13.setObjectName("label_13")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.catalog.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setEnabled(True)
        self.tab_4.setObjectName("tab_4")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 621))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_service = QtWidgets.QWidget()
        self.tab_service.setObjectName("tab_service")
        self.service_tableWidget = QtWidgets.QTableWidget(self.tab_service)
        self.service_tableWidget.setGeometry(QtCore.QRect(10, 60, 831, 411))
        self.service_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.service_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.service_tableWidget.setObjectName("service_tableWidget")
        self.service_tableWidget.setColumnCount(5)
        self.service_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.service_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.service_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.service_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.service_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.service_tableWidget.setHorizontalHeaderItem(4, item)
        self.service_tableWidget.verticalHeader().setVisible(False)
        self.service_label = QtWidgets.QLabel(self.tab_service)
        self.service_label.setGeometry(QtCore.QRect(280, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.service_label.setFont(font)
        self.service_label.setObjectName("service_label")
        self.guest_card_edit = QtWidgets.QLineEdit(self.tab_service)
        self.guest_card_edit.setGeometry(QtCore.QRect(10, 490, 251, 31))
        self.guest_card_edit.setObjectName("guest_card_edit")
        self.spinBox = QtWidgets.QSpinBox(self.tab_service)
        self.spinBox.setGeometry(QtCore.QRect(270, 490, 41, 31))
        self.spinBox.setObjectName("spinBox")
        self.arrangeButton = QtWidgets.QPushButton(self.tab_service)
        self.arrangeButton.setGeometry(QtCore.QRect(340, 490, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.arrangeButton.setFont(font)
        self.arrangeButton.setObjectName("arrangeButton")
        self.tabWidget.addTab(self.tab_service, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_4 = QtWidgets.QLabel(self.tab_9)
        self.label_4.setGeometry(QtCore.QRect(320, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tableWidget_invoice = QtWidgets.QTableWidget(self.tab_9)
        self.tableWidget_invoice.setGeometry(QtCore.QRect(70, 90, 741, 351))
        self.tableWidget_invoice.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_invoice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_invoice.setObjectName("tableWidget_invoice")
        self.tableWidget_invoice.setColumnCount(6)
        self.tableWidget_invoice.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoice.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoice.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoice.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoice.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoice.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_invoice.setHorizontalHeaderItem(5, item)
        self.tableWidget_invoice.verticalHeader().setVisible(False)
        self.label_5 = QtWidgets.QLabel(self.tab_9)
        self.label_5.setGeometry(QtCore.QRect(510, 450, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.resultAmount = QtWidgets.QLabel(self.tab_9)
        self.resultAmount.setGeometry(QtCore.QRect(620, 450, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resultAmount.setFont(font)
        self.resultAmount.setObjectName("resultAmount")
        self.guest_card_edit_book_2 = QtWidgets.QLineEdit(self.tab_9)
        self.guest_card_edit_book_2.setGeometry(QtCore.QRect(70, 450, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.guest_card_edit_book_2.setFont(font)
        self.guest_card_edit_book_2.setObjectName("guest_card_edit_book_2")
        self.invoice_pushButton = QtWidgets.QPushButton(self.tab_9)
        self.invoice_pushButton.setGeometry(QtCore.QRect(330, 450, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.invoice_pushButton.setFont(font)
        self.invoice_pushButton.setObjectName("invoice_pushButton")
        self.tabWidget.addTab(self.tab_9, "")
        self.catalog.addTab(self.tab_4, "")
        self.catalog_3 = QtWidgets.QWidget()
        self.catalog_3.setObjectName("catalog_3")
        self.status_button = QtWidgets.QPushButton(self.catalog_3)
        self.status_button.setGeometry(QtCore.QRect(250, 60, 351, 61))
        self.status_button.setObjectName("status_button")
        self.position_button = QtWidgets.QPushButton(self.catalog_3)
        self.position_button.setGeometry(QtCore.QRect(250, 140, 351, 61))
        self.position_button.setObjectName("position_button")
        self.categories_button = QtWidgets.QPushButton(self.catalog_3)
        self.categories_button.setGeometry(QtCore.QRect(250, 230, 351, 61))
        self.categories_button.setObjectName("categories_button")
        self.properties_button = QtWidgets.QPushButton(self.catalog_3)
        self.properties_button.setGeometry(QtCore.QRect(250, 310, 351, 61))
        self.properties_button.setObjectName("properties_button")
        self.rooms_button = QtWidgets.QPushButton(self.catalog_3)
        self.rooms_button.setGeometry(QtCore.QRect(240, 410, 361, 121))
        self.rooms_button.setObjectName("rooms_button")
        self.catalog.addTab(self.catalog_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.catalog.setCurrentIndex(1)
        self.passengers_tab.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hotel"))
        self.label.setText(_translate("MainWindow", "Регистрация гостя"))
        self.nameEdit.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.lastnameEdit.setPlaceholderText(_translate("MainWindow", "Фамилия"))
        self.phoneEdit.setPlaceholderText(_translate("MainWindow", "Номер телефона"))
        self.passportEdit.setPlaceholderText(_translate("MainWindow", "Паспорт"))
        self.dateofbirthEdit.setSpecialValueText(_translate("MainWindow", "Дата рождения"))
        self.addGuest_Button.setText(_translate("MainWindow", "Зарегестрировать"))
        self.nameEdit_payer.setPlaceholderText(_translate("MainWindow", "Имя плательщика"))
        self.lastnameEdit_payer.setPlaceholderText(_translate("MainWindow", "Фамилия плательщика"))
        self.passportEdit_payer.setPlaceholderText(_translate("MainWindow", "Паспорт плательщика"))
        self.passengers_tab.setTabText(self.passengers_tab.indexOf(self.addPassengers), _translate("MainWindow", "Регистрация гостя"))
        self.label_2.setText(_translate("MainWindow", "Поиск гостя"))
        self.search_nameEdit.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.search_lastnameEdit.setPlaceholderText(_translate("MainWindow", "Фамилия"))
        self.search_passportEdit.setPlaceholderText(_translate("MainWindow", "Паспорт"))
        self.searchButton.setText(_translate("MainWindow", "Найти"))
        item = self.searchResultTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.searchResultTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.searchResultTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.searchResultTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Телефон"))
        item = self.searchResultTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.searchResultTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Паспорт"))
        self.passengers_tab.setTabText(self.passengers_tab.indexOf(self.searchPassengers), _translate("MainWindow", "Поиск гостя"))
        item = self.guest_cards.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер карточки"))
        item = self.guest_cards.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.guest_cards.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.guest_cards.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Телефон"))
        item = self.guest_cards.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Дата рождения"))
        item = self.guest_cards.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Паспорт"))
        self.label_14.setText(_translate("MainWindow", "Клиенты"))
        self.passengers_tab.setTabText(self.passengers_tab.indexOf(self.tab_2), _translate("MainWindow", "Карточки гостей"))
        self.catalog.setTabText(self.catalog.indexOf(self.Passengers), _translate("MainWindow", "Гости"))
        item = self.room_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.room_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.room_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Категория"))
        item = self.room_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Этаж"))
        item = self.room_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Свойство"))
        item = self.room_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Детали"))
        self.label_3.setText(_translate("MainWindow", "Номера"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Список всех номеров"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Tab 2"))
        self.catalog.setTabText(self.catalog.indexOf(self.rooms), _translate("MainWindow", "Номера"))
        self.booking_departureDateEdit.setToolTip(_translate("MainWindow", "Дата выезда"))
        self.label_30.setText(_translate("MainWindow", "Бронирование"))
        self.addBookingButton.setText(_translate("MainWindow", "Добавить"))
        self.booking_arrivalDateEdit_2.setToolTip(_translate("MainWindow", "Дата заселения"))
        item = self.Booking.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.Booking.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.Booking.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Категория"))
        item = self.Booking.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.Booking.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Свойство"))
        item = self.Booking.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Описание"))
        self.guest_card_edit_book.setPlaceholderText(_translate("MainWindow", "Номер карточки гостя"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Бронирование"))
        self.searchBookingsButton.setText(_translate("MainWindow", "Найти"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата брони"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Категория"))
        item = self.searchBookinsResultTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Дата заселения"))
        self.label_13.setText(_translate("MainWindow", "Поиск брони"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Поиск брони"))
        self.catalog.setTabText(self.catalog.indexOf(self.tab), _translate("MainWindow", "Бронирование"))
        item = self.service_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.service_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.service_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.service_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.service_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Стоимость"))
        self.service_label.setText(_translate("MainWindow", "Оформление услуг"))
        self.guest_card_edit.setPlaceholderText(_translate("MainWindow", "Номер карточки гостя"))
        self.arrangeButton.setText(_translate("MainWindow", "Оформить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_service), _translate("MainWindow", "Оформление"))
        self.label_4.setText(_translate("MainWindow", "Счет за услуги"))
        item = self.tableWidget_invoice.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_invoice.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Услуга"))
        item = self.tableWidget_invoice.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget_invoice.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget_invoice.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.tableWidget_invoice.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Дата"))
        self.label_5.setText(_translate("MainWindow", "К оплате:"))
        self.resultAmount.setText(_translate("MainWindow", "TextLabel"))
        self.guest_card_edit_book_2.setPlaceholderText(_translate("MainWindow", "Номер карточки гостя"))
        self.invoice_pushButton.setText(_translate("MainWindow", "Найти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Счет"))
        self.catalog.setTabText(self.catalog.indexOf(self.tab_4), _translate("MainWindow", "Услуги"))
        self.status_button.setText(_translate("MainWindow", "Статусы"))
        self.position_button.setText(_translate("MainWindow", "Должности сотрудников"))
        self.categories_button.setText(_translate("MainWindow", "Категории номеров"))
        self.properties_button.setText(_translate("MainWindow", "Свойства номеров"))
        self.rooms_button.setText(_translate("MainWindow", "КОМНАТЫ"))
        self.catalog.setTabText(self.catalog.indexOf(self.catalog_3), _translate("MainWindow", "Справочники"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

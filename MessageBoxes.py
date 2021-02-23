import sys

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class QBoxes(QMessageBox):
    def noCon(self):
        QMessageBox.about(self, "Ошибка", "Отсутствует соединение")

    def noAccess(self):
        QMessageBox.about(self, "Ошибка", "Нет доступа")

    def wrongPass(self):
        QMessageBox.about(self, "Ошибка", "Некорректный логин/пароль")

    def notFound(self):
        QMessageBox.about(self, "Ошибка", "Не найдено")

    def userInfo(self,role):
        message = str()
        if role == '1':
            message = "Вы вошли как Администратор. У Вас доступ ко всем функциям."
        elif role == '2':
            message = "Вы вошли как Сотрубник. У Вас доступ к функциям: Добавить гостя, Найти гостя, Add flight, Add regular flight, Search flights, Search regular flights, Add booking, Search bookings, Check-in, Search check-ins"
        elif role == '3':
            message = "You logged in as Passenger. You have access to these functions: Search flight, Add booking for passenger,Check-In"
        QMessageBox.about(self, "Message", "Message:{0} ".format(message) )


class InfoBox(QMessageBox):
    def showBox(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Message box pop up window")
        msgBox.setWindowTitle("QMessageBox Example")

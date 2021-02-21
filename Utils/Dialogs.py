# -*- coding: utf-8 -*-
# Модуль диалоговых окон
import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QWidget, QTreeWidgetItem
from PyQt5 import QtWidgets, QtCore


# Сообщение: Фатальная ошибка. Продолжение выполнения невозможно
def MessageFatalError(ErrMessage):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(ErrMessage + "\nПродолжение выполнения программы невозможно.")
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle("Фатальная ошибка")
    msg.setWindowIcon(QIcon('Images\GraphIcon.png'))
    # msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()
    sys.exit(1)


# Сообщение: Предупреждение. Только кнопка OK
def MessageWarning(WarnMessage):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(WarnMessage)
    msg.setWindowTitle("Предупреждение.")
    msg.setWindowIcon(QIcon('Images\GraphIcon.png'))
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


# Сообщение: Информационное сообщение. Только кнопка ОК
def MessageInfo(InfoMessage):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(InfoMessage)
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle("Информационное сообщение.")
    msg.setWindowIcon(QIcon('Images\GraphIcon.png'))
    # msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()


# Сообщение: Вопрос. Только кнопки Да Нет
def MessageQuestionYesNo(QuestionMessage, Title="Запрос."):
    #    def msgbtn(i):
    #        ButtonText = i.text()
    #        if ButtonText == "Да" :#"&Yes":
    #            return True
    #        else:
    #            return False

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText(QuestionMessage)
    # msg.setInformativeText("This is additional information")
    msg.setWindowTitle(Title)
    msg.setWindowIcon(QIcon('Images\GraphIcon.png'))

    # msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.buttons()[0].setText("Да")
    msg.buttons()[1].setText("Нет")
    #    msg.buttonClicked.connect(msgbtn)
    tt = msg.exec_()
    if tt == QMessageBox.Yes:
        return True
    else:
        return False

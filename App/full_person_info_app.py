from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from forms import full_person_info # Это наш конвертированный файл дизайна
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import os
from Database.db import Database
from PyQt5.QtGui import QIcon
from Database.test_con import *


class Full_Person_Info_Form(QtWidgets.QMainWindow, full_person_info.Ui_Full_Person_Info_Form):
    def __init__(self, win):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.setupUiFeatures()  # добавление в дизайн новых фичей
        self.setFixedSize(self.size())
        self.__connectHandler()
        self.win = win
    
    # def __connectHandler(self):
    #     self.ok_button.clicked.connect(self.ok)
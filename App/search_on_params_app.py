from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from forms import search # Это наш конвертированный файл дизайна
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import os
from Database.db import Database
from PyQt5.QtGui import QIcon
from Database.test_con import *


class Search_Form(QtWidgets.QMainWindow, search.Ui_Search_Form):
    def __init__(self, win):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.setupUiFeatures()  # добавление в дизайн новых фичей
        self.setFixedSize(self.size())
        self.__connectHandler()
        self.win = win
    
    def __connectHandler(self):
        self.ok_button.clicked.connect(self.ok)
    
    def ok(self):
        s1 = ['p.surname', 'p.name', 'd.bd'][self.search_paramets_combobox.currentIndex()]
        s2 = self.search_parametr_lineedit.text()
        if s2 == '':
            QMessageBox.about(self, 'Ошибка', 'Введите параметр поиска')
        else:
            db = Database()
            data = db.search_person(s1, s2)
            if data != None:
                self.win.data = data
                self.win.fill_in_table()
                self.hide()
            else:
                QMessageBox.about(self, 'Внимание', 'Совпадений не найдено')
                self.hide()
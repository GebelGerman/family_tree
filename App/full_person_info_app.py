from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from forms import full_person_info # Это наш конвертированный файл дизайна
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import os
from Database.db import Database
from PyQt5.QtGui import QIcon
from Database.test_con import *


class Full_Person_Info_Form(QtWidgets.QMainWindow, full_person_info.Ui_Full_Person_Info_Form):
    def __init__(self, person_id):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.setupUiFeatures()  # добавление в дизайн новых фичей
        self.setFixedSize(self.size())
        self.db = Database()
        self.__connectHandler()
        self.person_id = person_id
        self.data = []
        self.update = False
    
    def __connectHandler(self):
        self.show_button.clicked.connect(self.show_other_surnames)
        self.update_rb.clicked.connect(self.set_visible_buttons)
        self.save_button.clicked.connect(self.save_other_surnames)

    def set_visible_buttons(self):
        flag = True
        if not self.update_rb.isChecked:
            flag = False
        self.save_button.setEnabled(flag)
    
    def fill_in_table(self):
        self.tableWidget.setRowCount(len(self.data)-1)
        self.tableWidget.setColumnCount(len(self.data[0]))
        self.tableWidget.setHorizontalHeaderLabels(self.data[0])
        r = 0
        for i in self.data[1:]:
            c = 0
            for j in i:
                self.tableWidget.setItem(r, c, QTableWidgetItem(str(j)))
                c += 1
            r += 1
    
    def show_other_surnames(self):
        self.data = self.db.select_other_surname_person(self.person_id)
        print(self.data)
        if self.data is None:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setHorizontalHeaderLabels(['other_surname', 
                                                            'other_name', 
                                                            'surname_and_name_after_baptism', 
                                                            'yard_nicknames'])
            self.update = False
        else:
            self.update = True
            self.fill_in_table()

    def save_other_surnames(self):
        data = []
        row = 0
        col = 0
        for i in range(4):
            try:
                data.append(self.tableWidget.item(row, col).text())
            except:
                data.append('')
            col += 1
        self.db.save_other_surname(data, self.person_id, self.update)
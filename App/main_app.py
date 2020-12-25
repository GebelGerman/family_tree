from Database.db import Database
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from forms import main_window # Это наш конвертированный файл дизайна
from PyQt5.QtWidgets import QTableWidgetItem
import os
from PyQt5.QtGui import QIcon
from Database.test_con import *
from App.search_on_params_app import Search_Form


class Main_App(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        #self.setupUiFeatures()  # добавление в дизайн новых фичей
        self.setFixedSize(self.size())
        self.__connectHandler()
        self.db = Database()

        #show all data
        self.show_all_person()
        self.search_form = Search_Form(self)
        
    def __connectHandler(self):
        # Buttons
        self.search_button.clicked.connect(self.search_person)
        self.update_button.clicked.connect(self.update_row_data)
        self.show_full_info_button.clicked.connect(self.show_full_person_info)
        self.show_all_documents_button.clicked.connect(self.show_all_documents)
        self.show_short_info_button.clicked.connect(self.show_short_info_person)
        self.show_all_person_button.clicked.connect(self.show_all_person)
        # Table
        self.tableWidget.itemSelectionChanged.connect(self.unenable_buttons)
        self.tableWidget.cellChanged.connect(self.tableWidget.resizeColumnsToContents)
        self.tableWidget.cellChanged.connect(self.set_id_col_hidden)
    
    def unenable_buttons(self):
        items = list(self.tableWidget.selectedItems())
        flag = True
        if len(items) == 0:
            flag = False
        self.update_button.setEnabled(flag)
        self.create_tree_button.setEnabled(flag)
        self.delete_button.setEnabled(flag)
        self.show_full_info_button.setEnabled(flag)
        self.show_all_documents_button.setEnabled(flag)
        self.show_short_info_button.setEnabled(flag)

    def set_id_col_hidden(self):
        self.tableWidget.setColumnHidden(0, True)

    def show_all_person(self):
        self.data = self.db.selectall()
        self.fill_in_table()

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
        
    def search_person(self):
        self.search_form.show()
    
    def get_id(self):
        row = self.tableWidget.currentRow()
        col = 0
        return self.tableWidget.item(row, col).text()
    
    def show_full_person_info(self):
        id = self.get_id()
        pass

    def update_row_data(self):
        id = self.get_id()
        print(id)
    
    def show_short_info_person(self):
        id = self.get_id()
        self.data = self.db.search_person('p.id', int(id))
        self.fill_in_table()
    
    def show_all_documents(self):
        id = self.get_id()
        self.data = self.db.select_all_documents_person(id)
        self.fill_in_table()


        




# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/xml/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_person_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_person_button.setGeometry(QtCore.QRect(20, 600, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_person_button.setFont(font)
        self.add_person_button.setObjectName("add_person_button")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setEnabled(False)
        self.update_button.setGeometry(QtCore.QRect(770, 640, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setEnabled(False)
        self.delete_button.setGeometry(QtCore.QRect(770, 680, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.create_tree_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_tree_button.setEnabled(False)
        self.create_tree_button.setGeometry(QtCore.QRect(460, 680, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.create_tree_button.setFont(font)
        self.create_tree_button.setObjectName("create_tree_button")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(20, 520, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 1041, 501))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.show_full_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_full_info_button.setEnabled(False)
        self.show_full_info_button.setGeometry(QtCore.QRect(460, 640, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_full_info_button.setFont(font)
        self.show_full_info_button.setObjectName("show_full_info_button")
        self.show_all_documents_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_all_documents_button.setEnabled(False)
        self.show_all_documents_button.setGeometry(QtCore.QRect(460, 600, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_all_documents_button.setFont(font)
        self.show_all_documents_button.setObjectName("show_all_documents_button")
        self.clean_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_button.setGeometry(QtCore.QRect(890, 520, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clean_button.setFont(font)
        self.clean_button.setObjectName("clean_button")
        self.show_all_person_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_all_person_button.setGeometry(QtCore.QRect(670, 520, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_all_person_button.setFont(font)
        self.show_all_person_button.setObjectName("show_all_person_button")
        self.show_short_info_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_short_info_button.setEnabled(False)
        self.show_short_info_button.setGeometry(QtCore.QRect(770, 600, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.show_short_info_button.setFont(font)
        self.show_short_info_button.setObjectName("show_short_info_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Семейное древо"))
        self.add_person_button.setText(_translate("MainWindow", "Добавить человека"))
        self.update_button.setText(_translate("MainWindow", "Изменить данные"))
        self.delete_button.setText(_translate("MainWindow", "Удалить "))
        self.create_tree_button.setText(_translate("MainWindow", "Создать семейное древо"))
        self.search_button.setText(_translate("MainWindow", "Поиск"))
        self.show_full_info_button.setText(_translate("MainWindow", "Посмотреть полную информацию"))
        self.show_all_documents_button.setText(_translate("MainWindow", "Показать все документы"))
        self.clean_button.setText(_translate("MainWindow", "Очистить таблицу"))
        self.show_all_person_button.setText(_translate("MainWindow", "Показать всех людей"))
        self.show_short_info_button.setText(_translate("MainWindow", "Посмотреть краткую информацию"))

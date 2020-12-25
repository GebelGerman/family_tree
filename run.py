""" File for start app """ 
import sys  # sys нужен для передачи argv в QApplication
from PyQt5.QtWidgets import QApplication, QMessageBox
from App.main_app import Main_App


def main():
    try:
        app = QApplication(sys.argv)  # Новый экземпляр QApplication
        window = Main_App()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        app.exec_()  # и запускаем приложение
    except UserWarning as err:
        print(str(err))


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
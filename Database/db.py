""" File for connection with database """ 

import mysql.connector 

class DatabaseMeta(type):
    _instances = []

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=DatabaseMeta):
    def __init__(self) -> None:
        super().__init__()
        self.create_connection()

    def create_connection(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )
        self.cursor = mydb.cursor

    # other funtional
    def select_person():
        pass


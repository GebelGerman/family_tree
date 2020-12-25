""" File for connection with database """ 
import pymysql

class DatabaseMeta(type):

    _instances = {}  # создавшиеся объекты

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
          # при создании объекта обновляет изменяемые поля
        return cls._instances[cls]

class Database(metaclass=DatabaseMeta):
    def __init__(self) -> None:
        super().__init__()
        self.__create_connection()

    def __create_connection(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='qwerty',
                             db='family_tree',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    def selectall(self):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """SELECT p.id, p.name as 'Имя', p.surname as 'Фамилия', 
                            p.gender as 'Пол', d.bd as 'Год рождения'
                            from person as p 
                            join dates as d on p.id = d.idPerson;"""
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
        self.connection.commit()
        return Database.to_table_view(result)
        

    # other funtional
    def search_person(self, s1, s2):
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = """SELECT p.id, p.name as 'Имя', p.surname as 'Фамилия', 
                        p.gender as 'Пол', e.name as 'Сословие', d.bd as 'Год рождения', 
                        s.first_name as 'Место проживания'
                        from person as p 
                        join estate as e on p.idEstate = e.id
                        join dates as d on p.id = d.idPerson
                        join (select sett.first_name, pl.idPerson 
                        from settlements as sett join places_of_residence as pl 
                        on sett.id = pl.idPlaceOfLiving) as s on p.id=s.idPerson
                        WHERE %s = \'%s\'""" % (s1, s2)
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
        self.connection.commit()
        return Database.to_table_view(result)

    @staticmethod
    def to_table_view(result):
        if len(result) != 0:
            rows_data = [list(result[0].keys())]
            for i in result:
                mini_data = []
                for j in rows_data[0]:
                    mini_data.append(i[j])
                rows_data.append(mini_data)
            # print(rows_data)
            return rows_data
        else: 
            return None

    def select_all_documents_person(self, person_id):
        with self.connection.cursor() as cursor:
            sql = """SELECT person.id, person.name, person.surname, res.page, res.persons_age, res.event_date, res.name, res.fond, 
                        res.register, res.delo, res.date, res.type, res.notes, res.mini_name, res.first_name FROM
                        (SELECT p.idPerson, p.page, p.persons_age, p.event_date, d.name, d.fond, d.register, d.delo, 
                        d.date, d.type, d.notes, d.mini_name, settlements.first_name FROM casez_sheet AS p
                        JOIN (SELECT documents.id, documents.name, documents.date, documents.type, documents.notes, documents.fond, documents.register, documents.delo, archives.mini_name
                        FROM archives JOIN documents ON archives.id = documents.idArchive) AS d ON d.id = p.idDocument
                        JOIN settlements ON settlements.id = p.idEvent_place) as res
                        JOIN person ON res.idPerson = person.id
                        WHERE person.id=%s""" % person_id
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
        self.connection.commit()
        return Database.to_table_view(result)
    
    def select_other_surname_person(self, person_id):
        with self.connection.cursor() as cursor:
            sql = """SELECT other_surname, other_name, surname_and_name_after_baptism, yard_nicknames
                        FROM other_surname WHERE idPerson = %s""" % person_id
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        self.connection.commit()
        return Database.to_table_view(result)

    def save_other_surname(self, data, person_id, update):
        print(data, person_id)
        with self.connection.cursor() as cursor:
            if update:
                sql = """UPDATE other_surname SET other_surname = %s, other_name = %s, 
                            urname_and_name_after_baptism = %s, yard_nicknames = %s WHERE idPerson = %s""" % (data[0], data[1], data[2], data[3], str(person_id))
            else:
                 sql = """INSERT INTO other_surname (idPerson, other_surname, other_name, surname_and_name_after_baptism, yard_nicknames)
                            VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')""" % (str(person_id), data[0], data[1], data[2], data[3])
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
        self.connection.commit()
        return Database.to_table_view(result)

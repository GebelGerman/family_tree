import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='qwerty',
                             db='fam_tree',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def selectall():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = """SELECT p.name as 'Имя', p.surname as 'Фамилия', 
                            p.gender as 'Пол', e.name as 'Сословие', 
                            d.bd as 'Год рождения', s.first_name as 'Место проживания'
                            from person as p 
                            join estate as e on p.idEstate = e.id
                            join date as d on p.id = d.idPerson
                            join (select sett.first_name, pl.idPerson from settlements as sett join places_of_residence as pl on sett.id = pl.idPlaceOfLiving) as s on p.id=s.idPerson;"""
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
        connection.commit()
    finally:
        connection.close()
    return result

def to_table_view(table):
    rows_data = [list(table[0].keys())]
    for i in table:
        mini_data = []
        for j in rows_data[0]:
            mini_data.append(i[j])
        rows_data.append(mini_data)
    print(rows_data)
    return rows_data


if __name__ == "__main__":
    table_view(selectall())
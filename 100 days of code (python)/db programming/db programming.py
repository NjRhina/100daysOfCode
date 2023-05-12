import sqlite3

class Persons:
    def __init__(self, id_number, first, last, age):

        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age

        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                age INTEGER
            )
                            """)


    def load_person(self, id_number):
        self.cursor.execute("""  SELECT * FROM persons WHERE id = {} """.format (id_number))
        results = self.cursor.fetchone()

        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("""
            INSERT INTO persons VALUES ({}, '{}', '{}', {})
            """.format(self.id_number, self.first, self.last, self.age))
        self.connection.commit()

p1 = Persons(4,'Nana', 'Namono',  34 )
p1.insert_person()

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("""  SELECT * FROM persons """)
results = cursor.fetchall()
print(results)

connection.close()



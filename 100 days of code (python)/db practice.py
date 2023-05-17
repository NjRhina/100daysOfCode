import sqlite3

class Toyota:
    def __init__(self, id, brand, engine, year ):
        self.id = id
        self.brand = brand
        self.engine = engine
        self.year = year

        # db connection
        self.conn = sqlite3.connect("cars.db")
        self.cursor = self.conn.cursor()
        # create the table to store our data
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS toyota (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                brand VARCHAR,
                                engine VARCHAR,
                                year INTEGER
                            )
                            """)

    # function that inserts data into the table
    def insertion(self):
        self.cursor.execute(
            """ INSERT INTO toyota VALUES ({}, '{}', '{}', {}) """.format(self.id, self.brand, self.engine, self.year)
                            )
        self.conn.commit()

    # function that reads all records from the database
    def retrieve_all(self):
        self.conn = sqlite3.connect("cars.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """ SELECT * FROM toyota """
        )
        # create a variable to store retrieved record
        results4many = self.cursor.fetchall()
        print(results4many)

    # function that reads a particular record from the database
    def retrieve_one(self,id):

        self.cursor.execute(
            """ SELECT * FROM toyota WHERE id = {}""".format(id)
                            )
        # create a variable to store retrieved record
        results4one = self.cursor.fetchone()

        #  retrieved records
        self.id = id
        self.brand = results4one[1]
        self.engine = results4one[2]
        self.year = results4one[3]

        print(results4one)

    # function that updates a record
    def update_record(self, id, brand, engine, year):
        self.cursor.execute(""" UPDATE toyota SET brand='{}', engine='{}', year={} WHERE id={} """.format(brand, engine, year,id))
        self.id = id
        self.brand = brand
        self.engine = engine
        self.year = year
        self.conn.commit()

    # function that deletes record
    def delete_record(self,id):
        self.cursor.execute(""" DELETE FROM toyota WHERE id = {} """.format(id))
        self.id = id
        self.conn.commit()

car1 = Toyota(15,"XTrail","Automatic", 2008)
car1.insertion()

car1.retrieve_all()
car1.retrieve_one(5)
car1.update_record(15, "Sienta", "Automatic", 2018)
car1.delete_record(8)
car1.retrieve_all()


import mysql.connector

class partDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def addPart(self, partNumber, partName, brand, price):
        query = "insert into part (part_number, part_name, brand, price) values (%s, %s, %s, %s)"
        self.cursor.execute(query, (partNumber, partName, brand, price))
        self.connection.commit()

    # def
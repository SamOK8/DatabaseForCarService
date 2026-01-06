import mysql.connector

class partDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add_part_for_transaction(self, part_number, part_name, brand, price):
        query = """
        insert into part (part_number, part_name, brand, price)
        values (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (part_number, part_name, brand, price))

    def addPart(self, part_number, part_name, brand, price, quantity):
        query = """
        insert into part (part_number, part_name, brand, price, quantity)
        values (%s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (part_number, part_name, brand, price, quantity))
        self.connection.commit()

    def findPartByNumber(self, part_number):
        query = "select * from part where part_number = %s"
        self.cursor.execute(query, (part_number,))
        return self.cursor.fetchall()

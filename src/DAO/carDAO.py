import mysql.connector

class carDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def addCar(self, vin, brand, model, year, engineType):
        query = "insert into car (vin, brand, model, year, engineType) values (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (vin, brand, model, year, engineType))
        self.connection.commit()

    def findCarByVin(self, vin):
        query = "select * from car where vin= %s"
        self.cursor.execute(query, (vin,))
        result = self.cursor.fetchall()
        return result
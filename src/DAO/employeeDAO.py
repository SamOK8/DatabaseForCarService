import mysql.connector

class employeeDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def addEmployee(self, surname, email):
        query = """
        INSERT INTO employee (surname, email)
        VALUES (%s, %s)
        """
        self.cursor.execute(query, (surname, email))
        self.connection.commit()

    # def findBy
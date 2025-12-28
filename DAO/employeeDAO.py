import mysql.connector

class employeeDAO:
    def __init__(self, connection):
        self.connection = connection
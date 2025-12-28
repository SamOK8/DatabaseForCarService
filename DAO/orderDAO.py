import mysql.connector

class orderDAO:
    def __init__(self, connection):
        self.connection = connection
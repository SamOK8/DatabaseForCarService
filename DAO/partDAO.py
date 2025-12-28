import mysql.connector

class partDAO:
    def __init__(self, connection):
        self.connection = connection
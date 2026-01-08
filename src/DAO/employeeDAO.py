import mysql.connector

class employeeDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def addEmployee(self, surname, email):
        query = """
        insert into employee (surname, email)
        values (%s, %s)
        """
        self.cursor.execute(query, (surname, email))
        self.connection.commit()

    def find_employee_by_email(self, email):
        query = "select * from employee where email= %s"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchall()
        return result
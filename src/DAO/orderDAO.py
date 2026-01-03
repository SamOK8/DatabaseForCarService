import mysql.connector

class orderDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add_service_order(self, car_id, employee_id, created_at, is_done):
        query = """
        INSERT INTO service_order (car_id, employee_id, created_at, is_done)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(
            query,
            (car_id, employee_id, created_at, is_done)
        )
        self.connection.commit()
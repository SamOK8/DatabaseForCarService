
class ServiceOrderPartDao:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def addPartToOrder(self, order_id, part_id, quantity):
        query = """
        INSERT INTO service_order__part (order_id, part_id, quantity)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (order_id, part_id, quantity))
        self.connection.commit()

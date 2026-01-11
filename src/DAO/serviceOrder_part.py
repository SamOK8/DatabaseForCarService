
class ServiceOrderPartDao:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add_part_to_order(self, order_id, part_id, quantity):
        query = """
        insert into service_order__part (order_id, part_id, quantity)
        values (%s, %s, %s)
        """
        self.cursor.execute(query, (order_id, part_id, quantity))

    def delete_parts_by_order(self, order_id):
        sql = "delete from service_order__part where order_id = %s"
        self.cursor.execute(sql, (order_id,))



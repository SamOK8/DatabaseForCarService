class orderDAO:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def add_service_order(self, car_id, employee_id, created_at, is_done):
        query = """
        insert into service_order (car_id, employee_id, created_at, is_done)
        values (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (car_id, employee_id, created_at, is_done))
        self.connection.commit()


    def delete_order(self, order_id):
        query = "delete from service_order where order_id = %s"
        self.cursor.execute(query, (order_id,))
        self.connection.commit()


    def get_all_orders(self):
        query = """
        select o.order_id, o.created_at, o.is_done,
               c.vin, c.brand, c.model, c.year
        from service_order o
        join car c on o.car_id = c.car_id
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_order_car(self, order_id, car_id):
        query = """
        update service_order
        set car_id = %s
        where order_id = %s
        """
        self.cursor.execute(query, (car_id, order_id))
        self.connection.commit()


    def get_all_orders_by_car_vin(self, vin):
        query = """
        select o.*
        from service_order o
        join car c on o.car_id = c.car_id
        where c.vin = %s
        """
        self.cursor.execute(query, (vin,))
        return self.cursor.fetchall()

    # view - objednavky ktere cekaji na dily, k tomu info o aute a o dilech ktere cybi - pouziti pro report
    def get_all_orders_waiting_for_parts(self):
        query = "select * from orders_missing_parts"
        self.cursor.execute(query)
        return self.cursor.fetchall()











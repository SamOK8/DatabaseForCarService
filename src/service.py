import json
import datetime

import mysql.connector
from DAO.orderDAO import orderDAO
from DAO.carDAO import carDAO
from DAO.partDAO import partDAO
from DAO.employeeDAO import employeeDAO
from DAO.serviceOrder_part import ServiceOrderPartDao

class Service:
    def __init__(self):
        with open('config.json') as config_json:
            self.config = json.load(config_json)
        self.conn = None
        self.connect()

    def connect(self):
        try:
            db_conf = self.config['database']
            self.conn = mysql.connector.connect(**db_conf)
            self.conn.autocommit = False

            self.car_dao = carDAO(self.conn)
            self.part_dao = partDAO(self.conn)
            self.emp_dao = employeeDAO(self.conn)
            self.order_dao = orderDAO(self.conn)
            self.order_part_dao = ServiceOrderPartDao(self.conn)
        except Exception as e:
            raise Exception(f"DB error: {e}")


    # 4.
    def addOrder(self, vin, brand, model, year, engineType, employee_id):
        car_data = self.car_dao.findCarByVin(vin)
        if not car_data:
            self.car_dao.addCar(vin, brand, model, year, engineType)

        self.order_dao.add_service_order(car_data(0), employee_id, datetime.datetime.now(), False)

    # transaction 5.
    # def addPartToOrder

    # report 6.
    # def

    # import 7.
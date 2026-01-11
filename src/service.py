import json
import csv
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
        self.csv_file_path = self.config['import_file_csv']
        self.json_file_path = self.config['import_file_json']

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
    def addOrder(self, vin, brand, model, year, engineType, email):
        if engineType not in ("petrol", "diesel", "electric"):
            raise ValueError("Invalid engine type")
        if year < 1900 or year > datetime.datetime.now().year:
            raise ValueError("Invalid year")

        car_data = self.car_dao.findCarByVin(vin)
        if not car_data:
            self.car_dao.addCar(vin, brand, model, year, engineType)
            car_data = self.car_dao.findCarByVin(vin)

        employee = self.emp_dao.find_employee_by_email(email)
        if not employee:
            raise Exception("employee not found")

        print(car_data[0][0])
        self.order_dao.add_service_order(car_data[0][0], employee[0][0], datetime.datetime.now(), False)

    def deleteOrder(self, vin):
        try:
            orders = self.order_dao.get_open_order_by_vin(vin)
            if not orders:
                raise Exception("Order not found, check VIN")

            order_id = orders[0][0]

            self.order_part_dao.delete_parts_by_order(order_id)

            self.order_dao.delete_order(order_id)

            self.conn.commit()

        except Exception as e:
            self.conn.rollback()
            raise Exception(f"Delete order failed: {e}")

    def get_order_info(self):
        return self.order_dao.get_all_orders()

    def edit_order_car(self, vin_of_car_in_order, vin, brand, model, year, engineType):
        car = self.car_dao.findCarByVin(vin)
        if not car:
            self.car_dao.addCar(vin, brand, model, year, engineType)
            car = self.car_dao.findCarByVin(vin)

        orders = self.order_dao.get_open_order_by_vin(vin_of_car_in_order)
        if not orders:
            raise Exception("Order not found, check vin")
        order_id = orders[0][0]
        car_id = car[0][0]

        self.order_dao.update_order_car(order_id, car_id)



    # transaction 5.
    def addPartToOrderTransaction(self, vin, part_number, part_name, brand, price, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if price <= 0:
            raise ValueError("Price must be positive")


        part = self.part_dao.findPartByNumber(part_number)
        if not part:
            self.part_dao.addPart(part_number, part_name, brand, price, 0)
            part = self.part_dao.findPartByNumber(part_number)

        orders = self.order_dao.get_open_order_by_vin(vin)
        if not orders:
            raise Exception("Order not found, check vin")

        part_id = part[0][0]
        order_id = orders[0][0]
        self.order_part_dao.add_part_to_order(order_id, part_id, quantity)



    # report 6.
    def getWaitingOrdersReport(self):
        rows = self.order_dao.get_all_orders_waiting_for_parts()

        report = []
        for r in rows:
            report.append({
                "order_id": r[0],
                "vin": r[1],
                "car_brand": r[2],
                "car_model": r[3],
                "part_number": r[4],
                "part_name": r[5],
                "required_quantity": r[6],
                "stock_quantity": r[7],
                "missing_quantity": r[8],
                "price": r[9],
                "missing_price": r[10]
            })

        return report

    # import 7.
    def importEmployeesFromCSV(self):
        try:
            with open(self.csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.emp_dao.addEmployee(
                        row['surname'],
                        row['email']
                    )
        except FileNotFoundError:
            raise Exception("CSV file not found")
        except KeyError:
            raise Exception("Invalid CSV format")


    def importPartsFromJSON(self):
        try:
            with open(self.json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                for part in data:
                    self.part_dao.addPart(
                        part['part_number'],
                        part.get('part_name'),
                        part.get('brand'),
                        part['price'],
                        part['quantity']
                    )
        except FileNotFoundError:
            raise Exception("JSON file not found")
        except KeyError:
            raise Exception("Invalid JSON format")


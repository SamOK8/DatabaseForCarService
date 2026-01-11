from service import Service


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number.")


def read_string(prompt):
    value = input(prompt).strip()
    if not value:
        raise ValueError("Input cannot be empty")
    return value


service = None
try:
    service = Service()
except Exception as e:
    print(f"{e}")

if service:
    choice = -1
    while choice != 0:
        print(
            "\nChoose what to do:\n"
            "0. Exit\n"
            "1. Add order\n"
            "2. Show orders\n"
            "3. Edit order (change car)\n"
            "4. Delete order\n"
            "5. Add part to order\n"
            "6. Show waiting orders report\n"
            "7. Import employees from csv\n"
            "8. Import parts from json"
        )

        choice = read_int("Your choice: ")

        try:
            if choice == 1:
                vin = read_string("VIN: ")
                brand = read_string("Car brand: ")
                model = read_string("Car model: ")
                year = read_int("Year: ")
                engine_type = read_string("Engine type (petrol/diesel/electric): ")
                email = read_string("Employee email: ")

                service.addOrder(vin, brand, model, year, engine_type, email)
                print("Order added successfully.")

            elif choice == 2:
                orders = service.get_order_info()
                for o in orders:
                    print(o)

            elif choice == 3:
                old_vin = read_string("VIN of existing order: ")

                new_vin = read_string("New VIN: ")
                brand = read_string("New car brand: ")
                model = read_string("New car model: ")
                year = read_int("New car year: ")
                engine_type = read_string("Engine type (petrol/diesel/electric): ")

                service.edit_order_car(
                    old_vin,
                    new_vin,
                    brand,
                    model,
                    year,
                    engine_type
                )
                print("Order updated successfully.")

            elif choice == 4:
                vin = read_string("VIN of order to delete: ")
                service.deleteOrder(vin)
                print("Order deleted successfully.")

            elif choice == 5:
                vin = read_string("VIN: ")
                part_number = read_int("Part number: ")
                part_name = read_string("Part name: ")
                brand = read_string("Part brand: ")
                price = float(input("Price: "))
                quantity = read_int("Quantity needed: ")

                service.addPartToOrderTransaction(
                    vin,
                    part_number,
                    part_name,
                    brand,
                    price,
                    quantity
                )
                print("Part added to order.")

            elif choice == 6:
                report = service.getWaitingOrdersReport()
                for r in report:
                    print(r)

            elif choice == 7:
                service.importEmployeesFromCSV()
                print("Employees imported successfully.")

            elif choice == 8:
                service.importPartsFromJSON()
                print("Parts imported successfully.")

            elif choice == 0:
                print("Goodbye!")

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")

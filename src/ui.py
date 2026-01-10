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
            "3. Add part to order\n"
            "4. Show waiting orders report\n"
            "5. Import employees from csv\n"
            "6. Import parts from json"
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

            elif choice == 4:
                report = service.getWaitingOrdersReport()
                for r in report:
                    print(r)

            elif choice == 5:
                service.importEmployeesFromCSV()

            elif choice == 6:
                service.importPartsFromJSON()

            elif choice == 0:
                print("Goodbye!")

            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"Error: {e}")

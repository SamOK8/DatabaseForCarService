# project name

## Basic info
### author
- Samuel Hennel  
- email: saminkoh@gmail.com


- this is a school project for - Secondary Technical School of Electrical Engineering Jecna 30, Prague  
date - 10.1.2026

## How to run
- look in readme.txt

## configuration
### config.json
- Database
  - host - ip adress of db server  
  - user - username  
  - password  
  - database - name of database  
- App
  - import_file_json - name of json file for import, it needs to be in the same folder as the program(import of parts)  
  - import_file_csv - same as json but for  csv(import of employees)

## Requirements
### Functional requirements
- The application allows creation, modification, deletion and listing of service orders.
- A service order consists of data stored in multiple database tables (car, service_order, service_order__part).
- The application allows adding parts to an existing service order.
- The application allows importing employees from a CSV file.
- The application allows importing parts from a JSON file.
- The application generates a report of service orders that cannot be completed due to missing parts.
- The application uses at least one database transaction spanning multiple tables.

### Non-functional requirements
- The application is implemented in Python.
- The application uses a relational database system (MySQL).
- Database access is separated using the DAO pattern.
- Application configuration is stored in an external configuration file.
- The application handles invalid input data and database connection errors.
- The application can be distributed as a standalone executable file.

## Used technologies and libraries
- Python 3  
- MySQL – relational database system  
- mysql-connector-python – database driver for MySQL  
- CSV module – import of employee data  
- JSON module – import of parts data  
- PyInstaller – creation of standalone executable file

## Architecture
### layers
1. DAO
2. service
3. ui

## Behavior description
- The application starts and loads configuration from config.json.  
- A connection to the database is established.  
- The user interacts with the application through the UI.  
- User actions (e.g. creating an order, adding a part) are processed by the service layer.  
- The service layer validates input data and calls appropriate DAO methods.  
- DAO classes execute SQL queries on the database.  
- Results are returned back through the service layer to the UI.

## Import
### CSV - employees
#### example:  
    surname,email  
    Novak,novak@email.cz  
    Svoboda,svoboda@email.cz  
    Dvorak,dvorak@email.cz  

### JSON - parts
#### example:
    [  
      {  
        "part_number": 1001,  
        "part_name": "Brake pads",  
        "brand": "Brembo",  
        "price": 1200,
        "quantity": 5
       },
      {
        "part_number": 1002,
        "part_name": "Oil filter",
        "brand": "Bosch",
        "price": 300,
        "quantity": 20
      }
    ]

## Errors
- Invalid user input (empty fields, invalid data types, invalid values)  
- Missing or invalid import files (CSV / JSON)  
- Missing config file  
- Wrong config

## license
- This project is a school project created for educational purposes only.  
- The source code is not intended for commercial use.
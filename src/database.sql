create table car (
car_id int auto_increment primary key,
vin varchar(17) unique not null,
brand varchar(30) not null,
model varchar(30) not null,
year int not null,
engineType ENUM('petrol', 'diesel', 'electric')
);

create table part (
part_id int auto_increment primary key,
part_number int not null,
part_name varchar(40),
brand varchar(30),
price float not null,
quantity int not null default 0
);

create table employee (
employee_id int auto_increment primary key,
surname varchar(40) not null,
email varchar(50) unique
);

create table service_order (
order_id int auto_increment primary key,
car_id INT NOT NULL,
employee_id INT NOT NULL,
created_at DATETIME NOT NULL,
is_done bool not null default false,

FOREIGN KEY (car_id) REFERENCES car(car_id),
FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

-- M:N
create table service_order__part (
service_order_part_id INT AUTO_INCREMENT PRIMARY KEY,
order_id INT NOT NULL,
part_id INT NOT NULL,
quantity INT NOT NULL,

FOREIGN KEY (order_id) REFERENCES service_order(order_id),
FOREIGN KEY (part_id) REFERENCES part(part_id),
UNIQUE (order_id, part_id)
);




create view employee_orders_count as
select
    e.employee_id,
    e.surname,
    count(o.order_id) as orders_count
from employee e
left join service_order o on e.employee_id = o.employee_id
group by e.employee_id, e.surname;

create view orders_missing_parts as
select
    o.order_id,
    c.vin,
    c.brand as car_brand,
    c.model as car_model,

    p.part_number,
    p.part_name,

    sop.quantity as required_quantity,
    p.quantity as stock_quantity,
    (sop.quantity - p.quantity) as missing_quantity,

    p.price,
    (sop.quantity - p.quantity) * p.price as missing_price
from service_order o
join car c on o.car_id = c.car_id
join service_order__part sop on o.order_id = sop.order_id
join part p on sop.part_id = p.part_id
where
    o.is_done = false
    and sop.quantity > p.quantity;

DROP DATABASE IF EXISTS coffee_shop;
CREATE DATABASE coffee_shop;
USE coffee_shop;

CREATE TABLE employee (
employee_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE,
phone VARCHAR(20),
salary DECIMAL(10,2) NOT NULL,
manager_id INT,
FOREIGN KEY (manager_id) REFERENCES employee(employee_id) ON DELETE SET NULL
);

CREATE TABLE skill (
skill_id INT AUTO_INCREMENT PRIMARY KEY,
skill_name VARCHAR(50) NOT NULL,
description VARCHAR(100)
);

CREATE TABLE employee_skill (
employee_id INT,
skill_id INT,
PRIMARY KEY (employee_id, skill_id),
FOREIGN KEY (employee_id) REFERENCES employee(employee_id) ON DELETE CASCADE,
FOREIGN KEY (skill_id) REFERENCES skill(skill_id) ON DELETE CASCADE
);

CREATE TABLE equipment (
equipment_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
description VARCHAR(100)
);

CREATE TABLE employee_equipment (
employee_id INT,
equipment_id INT,
PRIMARY KEY (employee_id, equipment_id),
FOREIGN KEY (employee_id) REFERENCES employee(employee_id) ON DELETE CASCADE,
FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id) ON DELETE CASCADE
);

CREATE TABLE customer (
customer_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE,
phone VARCHAR(20)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE
);

CREATE TABLE roaster (
roaster_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
city VARCHAR(50),
country VARCHAR(50)
);

CREATE TABLE bean (
bean_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
roaster_id INT,
FOREIGN KEY (roaster_id) REFERENCES roaster(roaster_id) ON DELETE SET NULL
);

CREATE TABLE product (
product_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
category VARCHAR(50),
price DECIMAL(10,2) NOT NULL,
bean_id INT,
FOREIGN KEY (bean_id) REFERENCES bean(bean_id) ON DELETE SET NULL
);

CREATE TABLE order_item (
order_id INT,
product_id INT,
quantity INT NOT NULL,
price DECIMAL(10,2) NOT NULL,
PRIMARY KEY (order_id, product_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
);

CREATE TABLE payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT UNIQUE,
    method ENUM('cash','card','online') NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    payment_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

CREATE TABLE flavor_note (
flavor_note_id INT AUTO_INCREMENT PRIMARY KEY,
flavor VARCHAR(100) NOT NULL
);

CREATE TABLE bean_flavor_note (
bean_id INT,
flavor_note_id INT,
PRIMARY KEY (bean_id, flavor_note_id),
FOREIGN KEY (bean_id) REFERENCES bean(bean_id) ON DELETE CASCADE,
FOREIGN KEY (flavor_note_id) REFERENCES flavor_note(flavor_note_id) ON DELETE CASCADE
);

CREATE VIEW order_total AS
SELECT
order_id,
SUM(quantity * price) AS total
FROM order_item
GROUP BY order_id;

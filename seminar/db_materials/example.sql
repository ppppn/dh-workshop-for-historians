# create an example database
CREATE DATABASE example1;

# change to the example database
USE example1;

# set charset
SET NAMES 'utf8';

# create tables
CREATE TABLE orderers (
    id INT PRIMARY KEY,
    name VARCHAR(80),
    address VARCHAR(120),
    phone_no VARCHAR(11)
);

CREATE TABLE products(
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price INT
);

CREATE TABLE orders(
    id INT PRIMARY KEY,
    date DATE,
    orderer_id INT
);

CREATE TABLE sales(
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    amount INT
);

# check tables
SHOW TABLES;

SHOW COLUMNS FROM orderers;
SHOW COLUMNS FROM products;
SHOW COLUMNS FROM orders;
SHOW COLUMNS FROM sales;

# insert datasets
INSERT INTO orderers (id, name, address, phone_no) VALUES(1, '山田太郎', '東京都大田区', '08000000000');
INSERT INTO orderers (id, name, address, phone_no) VALUES(2, '佐藤花子', '東京都豊島区', '03000000000');

SELECT * FROM orderers;


INSERT INTO products (id, name, price) VALUES (1, 'トランプ', 200);
INSERT INTO products (id, name, price) VALUES (2, '家庭用花火', 1000);
INSERT INTO products (id, name, price) VALUES (3, 'マグカップ', 300);
INSERT INTO products (id, name, price) VALUES (4, '鉛筆', 200);
INSERT INTO products (id, name, price) VALUES (5, '消しゴム', 100);
INSERT INTO products (id, name, price) VALUES (6, '定規', 100);
INSERT INTO products (id, name, price) VALUES (7, '辞書', 3000);
INSERT INTO products (id, name, price) VALUES (8, 'サッカーボール', 1000);

SELECT * FROM products;


INSERT INTO orders (id, date, orderer_id) VALUES(1, '2018/10/1', 1);
INSERT INTO orders (id, date, orderer_id) VALUES(2, '2018/10/3', 2);

SELECT * FROM orders;


INSERT INTO sales (id, order_id, product_id, amount) VALUES(1, 1, 1, 10);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(2, 1, 2, 10);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(3, 1, 3, 20);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(4, 2, 4, 10);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(5, 2, 5, 10);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(6, 2, 6, 10);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(7, 2, 7, 10);
INSERT INTO sales (id, order_id, product_id, amount) VALUES(8, 2, 8, 10);

SELECT * FROM sales;


# do SELECTs
# 1. join all tables
SELECT 
    orders.id AS orders_id, 
    orders.date AS orders_date,
    sales.id AS sales_id, 
    products.id AS products_id, 
    products.name AS products_name, 
    products.price AS products_price,
    sales.amount AS sales_price, 
    products.price * sales.amount AS proceed, 
    orderers.id AS orderers_id, 
    orderers.name AS orderers_name, 
    orderers.address AS orderers_address, 
    orderers.phone_no AS orderers_phone_no
FROM 
    orders 
    JOIN sales ON orders.id = sales.order_id 
    JOIN products ON sales.product_id = products.id 
    JOIN orderers ON orderers.id = orders.orderer_id;

# 2. search the records orderes.id = 1
SELECT 
    orders.id AS orders_id, 
    orders.date AS orders_date,
    sales.id AS sales_id, 
    products.id AS products_id, 
    products.name AS products_name, 
    products.price AS products_price,
    sales.amount AS sales_price, 
    products.price * sales.amount AS proceed, 
    orderers.id AS orderers_id, 
    orderers.name AS orderers_name, 
    orderers.address AS orderers_address, 
    orderers.phone_no AS orderers_phone_no
FROM 
    orders 
    JOIN sales ON orders.id = sales.order_id 
    JOIN products ON sales.product_id = products.id 
    JOIN orderers ON orderers.id = orders.orderer_id 
WHERE
    orderers.id = 1;

# 3. count records
SELECT 
    count(*) AS num_sales
FROM sales;

# 4. count records with grouping
SELECT 
    orders.id AS orders_id, 
    count(*) AS num_sales
FROM
    orders JOIN sales ON orders.id = sales.order_id
GROUP BY
    orders.id;

# 5. sum
SELECT
    SUM(products.price * sales.amount) AS total_proceed
FROM
    products JOIN sales ON products.id = sales.product_id;

# LABs
# 1. SELECT without JOIN

SELECT 
    orders.id AS orders_id, 
    orders.date AS orders_date,
    sales.id AS sales_id, 
    products.id AS products_id, 
    products.name AS products_name, 
    products.price AS products_price,
    sales.amount AS sales_price, 
    products.price * sales.amount AS proceed, 
    orderers.id AS orderers_id, 
    orderers.name AS orderers_name, 
    orderers.address AS orderers_address, 
    orderers.phone_no AS orderers_phone_no
FROM 
    orders,
    sales, 
    products, 
    orderers;

# 2. SELECT with WHERE instead of JOIN

SELECT 
    orders.id AS orders_id, 
    orders.date AS orders_date,
    sales.id AS sales_id, 
    products.id AS products_id, 
    products.name AS products_name, 
    products.price AS products_price,
    sales.amount AS sales_price, 
    products.price * sales.amount AS proceed, 
    orderers.id AS orderers_id, 
    orderers.name AS orderers_name, 
    orderers.address AS orderers_address, 
    orderers.phone_no AS orderers_phone_no
FROM 
    orders,
    sales, 
    products, 
    orderers
WHERE
    orders.id = sales.order_id AND
    sales.product_id = products.id AND
    orderers.id = orders.orderer_id;

# 3. VIEW
CREATE VIEW full_list AS 
SELECT 
    orders.id AS orders_id, 
    orders.date AS orders_date,
    sales.id AS sales_id, 
    products.id AS products_id, 
    products.name AS products_name, 
    products.price AS products_price,
    sales.amount AS sales_price, 
    products.price * sales.amount AS proceed, 
    orderers.id AS orderers_id, 
    orderers.name AS orderers_name, 
    orderers.address AS orderers_address, 
    orderers.phone_no AS orderers_phone_no
FROM 
    orders 
    JOIN sales ON orders.id = sales.order_id 
    JOIN products ON sales.product_id = products.id 
    JOIN orderers ON orderers.id = orders.orderer_id;
CREATE TABLE items
(
    Id SERIAL PRIMARY KEY,
    Name CHARACTER VARYING(30),
	Price INTEGER
);
INSERT INTO items (Name, Price) VALUES ('Small Desk', 100);
INSERT INTO items (Name, Price) VALUES ('Large desk', 300);
INSERT INTO items (Name, Price) VALUES ('Fan', 80);

CREATE TABLE customers
(
    Id SERIAL PRIMARY KEY,
    First_Name CHARACTER VARYING(30),
    Last_Name CHARACTER VARYING(30)
);

INSERT INTO customers (First_Name, Last_Name) VALUES ('Greg', 'Jones');
INSERT INTO customers (First_Name, Last_Name) VALUES ('Sandra', 'Jones');
INSERT INTO customers (First_Name, Last_Name) VALUES ('Scott', 'Scott');
INSERT INTO customers (First_Name, Last_Name) VALUES ('Trevor', 'Green');
INSERT INTO customers (First_Name, Last_Name) VALUES ('Melanie', 'Johnson');

SELECT * FROM customers;
SELECT * FROM items;
SELECT * FROM items WHERE price > 80;
SELECT * FROM items WHERE price <= 300;
SELECT * FROM customers WHERE Last_Name = 'Jones';
SELECT * FROM customers WHERE Last_Name = 'Smith';
SELECT * FROM customers WHERE NOT First_Name = 'Scott';
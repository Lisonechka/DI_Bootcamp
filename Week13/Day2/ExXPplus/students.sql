CREATE TABLE students
(
    Id SERIAL PRIMARY KEY,
    First_Name CHARACTER VARYING(30),
    Last_Name CHARACTER VARYING(30),
    Birth_date DATE
);

INSERT INTO students (first_name, last_name, Birth_date) 
VALUES('Marc','Benichou','11/02/1998'), 
('Yoan', 'Cohen', '12/03/2010'),
('Lea', 'Benichou', '07/27/1987'),
('Amelia','Dux','04/07/1996'), 
('David', 'Grez', '06/14/2003'),
('Omer', 'Simpson', '10/03/1980');

SELECT * FROM students;

INSERT INTO students (first_name, last_name, birth_date) VALUES ('Liza', 'Malevich', '10/31/1987');
SELECT * FROM students;

SELECT first_name, last_name FROM students;

SELECT first_name, last_name FROM students WHERE id = 2;
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a%';
SELECT first_name, last_name FROM students WHERE first_name LIKE 'A%';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a';
SELECT first_name, last_name FROM students WHERE first_name LIKE '%a_';


SELECT first_name, last_name FROM students WHERE id=1 OR id=3;

SELECT first_name, last_name FROM students WHERE birth_date >= '01/01/2000';




SELECT * FROM students LIMIT 4;

SELECT first_name, last_name, birth_date FROM students WHERE birth_date = (SELECT max(birth_date) FROM students);

SELECT * FROM students LIMIT 3 OFFSET 2;





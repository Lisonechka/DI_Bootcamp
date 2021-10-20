CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

SELECT * FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('Matt','Damon','08/10/1970', 5);
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('George','Clooney','06/05/1961', 2);
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('Helen','Mirren','07/26/1945', 1);
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('Hilary','Swank','07/30/1974', 2);
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('Clinton','Eastwood','05/31/1930', 5), ('Allen', 'Woody', '11/30/1935', 4), ('Jack', 'Nicholson', '04/22/1937', 3);
SELECT * FROM actors;
SELECT COUNT(*) as count FROM actors;
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES('Katharine','Hepburn', ' ', 4);



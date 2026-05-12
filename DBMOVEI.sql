DROP DATABASE IF EXISTS new_database;

CREATE DATABASE new_database;
USE new_database;

CREATE TABLE production (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    address VARCHAR(255)
);

INSERT INTO production (name, address) VALUES
('Paramount Pictures', 'Hollywood, USA'),
('Netflix Studios', 'Los Angeles, USA'),
('Marvel Studios', 'Burbank, USA');

CREATE TABLE director (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL
);

INSERT INTO director (name, birth_date) VALUES
('Christopher Nolan', '1970-07-30'),
('James Cameron', '1954-08-16'),
('Quentin Tarantino', '1963-03-27');

CREATE TABLE actor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL
);

INSERT INTO actor (name, birth_date) VALUES
('Leonardo DiCaprio', '1974-11-11'),
('Christian Bale', '1974-01-30'),
('Brad Pitt', '1963-12-18');

CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    release_year INT,
    duration TIME,
    production_id INT,
    director_id INT,
    FOREIGN KEY (production_id) REFERENCES production(id),
    FOREIGN KEY (director_id) REFERENCES director(id)
);

INSERT INTO movie (title, release_year, duration, production_id, director_id) VALUES
('Inception', 2010, '02:28:00', 2, 1),
('Interstellar', 2014, '02:49:00', 2, 1),
('The Dark Knight', 2008, '02:32:00', 1, 1),
('Avatar', 2009, '02:42:00', 3, 2),
('Titanic', 1997, '03:14:00', 3, 2);

CREATE TABLE movie_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_type VARCHAR(100) NOT NULL
);

INSERT INTO movie_type (name_type) VALUES
('Action'),
('Drama'),
('Sci-Fi'),
('Romance');

CREATE TABLE movie_movie_type (
    movie_id INT,
    type_id INT,
    PRIMARY KEY (movie_id, type_id),
    FOREIGN KEY (movie_id) REFERENCES movie(id),
    FOREIGN KEY (type_id) REFERENCES movie_type(id)
);

INSERT INTO movie_movie_type VALUES
(1, 3),
(2, 3),
(3, 1),
(4, 3),
(5, 4);

CREATE TABLE movie_actor (
    movie_id INT,
    actor_id INT,
    role VARCHAR(255),
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES movie(id),
    FOREIGN KEY (actor_id) REFERENCES actor(id)
);

INSERT INTO movie_actor VALUES
(1, 1, 'Cobb'),
(3, 2, 'Batman'),
(5, 3, 'Jack');

CREATE TABLE quote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    actor_id INT,
    text TEXT,
    FOREIGN KEY (movie_id) REFERENCES movie(id),
    FOREIGN KEY (actor_id) REFERENCES actor(id)
);

INSERT INTO quote (movie_id, actor_id, text) VALUES
(1, 1, 'You mustn’t be afraid to dream a little bigger.'),
(3, 2, 'I am Batman.'),
(5, 3, 'I will never let go.');
USE new_database;
------
UPDATE movie
SET title = 'New Title'
WHERE id = 2;

UPDATE movie
SET title = 'New Title'
WHERE id = 2;
UPDATE movie
SET title = 'Inception 2'
WHERE id = 1;
------------------------------
SELECT * FROM movie;
UPDATE movie
SET release_year = 2018
WHen release_year IN (2010, 2014);

SELECT * FROM movie;
UPDATE movie
SET title = 'Inception Returns',
    release_year = 2018
WHERE id = 1;
SELECT * FROM movie;
SELECT id, name
FROM production
WHERE name IN ('Paramount Pictures', 'Netflix Studios');
SELECT id AS productionnum
FROM production;
ALTER TABLE actor
ADD bonus INT;
ALTER TABLE actor
ADD salary INT;
UPDATE actor
SET bonus = salary * 0.10;
UPDATE actor SET salary = 50000 WHERE id = 1;
UPDATE actor SET salary = 60000 WHERE id = 2;
UPDATE actor SET salary = 70000 WHERE id = 3;
UPDATE actor
SELECT 
    id,
    name,
    salary,
    salary * 0.10 AS bonus
FROM actor;
SELECT 
    id,
    name,
    salary,
    salary * 0.10 AS bonus
FROM actor;
DROP DATABASE IF EXISTS newdatabase;

CREATE DATABASE newdatabase;
USE newdatabase;

CREATE TABLE production (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    address VARCHAR(255),
    region VARCHAR(100)
);

INSERT INTO production (name, address, region) VALUES
('Paramount Pictures', 'USA', 'USA'),
('Netflix Studios', 'USA', 'USA'),
('Marvel Studios', 'USA', 'USA'),
('Warner Bros', 'USA', 'USA'),
('Universal Pictures', 'USA', 'USA'),
('Sony Pictures', 'USA', 'USA'),
('Disney Studios', 'USA', 'USA'),
('Lionsgate', 'USA', 'USA'),
('DreamWorks', 'USA', 'USA'),
('Pixar', 'USA', 'USA');

CREATE TABLE director (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL
);

INSERT INTO director (name, birthdate) VALUES
('Christopher Nolan', '1970-07-30'),
('James Cameron', '1954-08-16'),
('Quentin Tarantino', '1963-03-27'),
('Steven Spielberg', '1946-12-18'),
('Martin Scorsese', '1942-11-17'),
('Ridley Scott', '1937-11-30'),
('Peter Jackson', '1961-10-31'),
('David Fincher', '1962-08-28'),
('Denis Villeneuve', '1967-10-03'),
('James Gunn', '1966-08-05');

CREATE TABLE actor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL,
    salary INT,
    bonus INT
);

INSERT INTO actor (name, birthdate, salary, bonus) VALUES
('Leonardo DiCaprio', '1974-11-11', 50000, 5000),
('Brad Pitt', '1963-12-18', 60000, 6000),
('Christian Bale', '1974-01-30', 55000, 5500),
('Robert Downey Jr', '1965-04-04', 80000, 8000),
('Tom Cruise', '1962-07-03', 90000, 9000),
('Johnny Depp', '1963-06-09', 45000, 4500),
('Will Smith', '1968-09-25', 70000, 7000),
('Matt Damon', '1970-10-08', 65000, 6500),
('Hugh Jackman', '1968-10-12', 75000, 7500),
('Chris Hemsworth', '1983-08-11', 85000, 8500);

CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(300) NOT NULL,
    releaseyear INT,
    duration TIME,
    productionid INT,
    directorid INT,
    FOREIGN KEY (productionid) REFERENCES production(id),
    FOREIGN KEY (directorid) REFERENCES director(id)
);

INSERT INTO movie (title, releaseyear, duration, productionid, directorid) VALUES
('Inception', 2010, '02:28:00', 2, 1),
('Interstellar', 2014, '02:49:00', 2, 1),
('The Dark Knight', 2008, '02:32:00', 1, 1),
('Avatar', 2009, '02:42:00', 3, 2),
('Titanic', 1997, '03:14:00', 3, 2),
('Joker', 2019, '02:02:00', 4, 8),
('Dune', 2021, '02:35:00', 9, 9),
('Avengers Endgame', 2019, '03:01:00', 3, 10),
('Gladiator', 2000, '02:35:00', 5, 6),
('The Wolf of Wall Street', 2013, '03:00:00', 6, 5);

CREATE TABLE movietype (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nametype VARCHAR(100)
);

INSERT INTO movietype (nametype) VALUES
('Action'),
('Drama'),
('Sci-Fi'),
('Romance'),
('Thriller'),
('Adventure'),
('Crime'),
('Fantasy'),
('Biography'),
('Comedy');

CREATE TABLE moviemovietype (
    movieid INT,
    typeid INT,
    PRIMARY KEY (movieid, typeid),
    FOREIGN KEY (movieid) REFERENCES movie(id),
    FOREIGN KEY (typeid) REFERENCES movietype(id)
);

INSERT INTO moviemovietype VALUES
(1,3),(2,3),(3,1),(4,3),(5,4),
(6,7),(7,3),(8,1),(9,1),(10,2);

CREATE TABLE movieactor (
    movieid INT,
    actorid INT,
    role VARCHAR(255),
    PRIMARY KEY (movieid, actorid),
    FOREIGN KEY (movieid) REFERENCES movie(id),
    FOREIGN KEY (actorid) REFERENCES actor(id)
);

INSERT INTO movieactor VALUES
(1,1,'Cobb'),
(2,8,'Cooper'),
(3,3,'Batman'),
(4,5,'Jake'),
(5,6,'Jack'),
(6,1,'Arthur'),
(7,7,'Paul'),
(8,10,'Thor'),
(9,2,'Maximus'),
(10,4,'Jordan');

CREATE TABLE quote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    movieid INT,
    actorid INT,
    text TEXT,
    FOREIGN KEY (movieid) REFERENCES movie(id),
    FOREIGN KEY (actorid) REFERENCES actor(id)
);

INSERT INTO quote (movieid, actorid, text) VALUES
(1,1,'You mustn’t be afraid to dream a little bigger.'),
(2,8,'Stay.'),
(3,3,'I am Batman.'),
(4,5,'I see you.'),
(5,6,'I will never let go.'),
(6,1,'One simple trick.'),
(7,7,'The spice must flow.'),
(8,10,'We are Groot.'),
(9,2,'What we do in life echoes in eternity.'),
(10,4,'I’m the king of the world.');
SELECT DISTINCT name, address
FROM production;
SELECT*FROM movie limit 2;
select*from movie where duration>40 and duration<1 ;
select*from movie where duration>40 or duration<1 ;
USE new_database;
SELECT *
FROM actor
WHERE salary > ANY (SELECT salary FROM actor WHERE salary < 60000);
SELECT *
FROM movie
WHERE title LIKE '%r';
SELECT *
FROM actor
WHERE salary IS NULL;
SELECT *
FROM actor
WHERE salary IS not NULL;
SELECT *
FROM movie
ORDER BY title ASC;
--------
#Retrieve movies that feature both Actor 1 and Actor 2 in the same movie (without JOIN).---solution:###
###it mean common movies of both actors:###
SHOW TABLES;
SELECT movie_id
FROM movie_actor
WHERE actor_id = 1
AND movie_id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 2
);
SELECT movie_id
FROM movie_actor
WHERE actor_id = 1
AND movie_id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 2
);
###Retrieve movies whose duration is greater than ANY Sci-Fi movie duration###
SELECT *
FROM movie_type n
WHERE n.name_type = 'Sci-Fi';
SELECT *
FROM movie
WHERE id IN (
    SELECT movieid
    FROM movie_movie_type
    WHERE typeid = (
        SELECT id
        FROM movie_type
        WHERE name_type = 'Sci-Fi'
    )
);
USE new_database;
SHOW TABLES;
SELECT movie_id
FROM movie_actor
WHERE actor_id = 1
AND movie_id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 2
);
#1

SELECT title
FROM movie
WHERE production_id IN (
    SELECT id
    FROM production
    WHERE address LIKE '%USA%'
);
#2

SELECT *
FROM movie
WHERE duration > ALL (
    SELECT duration
    FROM movie
    WHERE release_year = 2014
);
#3 Retrieve movies whose duration is greater than ANY Sci-Fi movie duration.
SELECT *
FROM movie
WHERE duration > ANY (
    SELECT duration
    FROM movie
    WHERE id IN (
        SELECT movie_id
        FROM movie_movie_type
        WHERE type_id = (
            SELECT id
            FROM movie_type
            WHERE name_type = 'Sci-Fi'
        )
    )
);
#4 Find movies that have NOT been acted in by "Keanu Reeves".
SELECT title
FROM movie
WHERE id NOT IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = (
        SELECT id
        FROM actor
        WHERE name = 'Keanu Reeves'
    )
);
#5Retrieve actors who have never acted in any movie.
SELECT *
FROM actor
WHERE id NOT IN (
    SELECT actor_id
    FROM movie_actor
);
#6

SELECT *
FROM movie
WHERE duration = (
    SELECT MAX(duration)
    FROM movie
);
#7

SELECT *
FROM movie
WHERE duration > (
    SELECT AVG(duration)
    FROM movie
);
#8
SELECT *
FROM movie
WHERE id NOT IN (
    SELECT movie_id
    FROM movie_movie_type
);
#9
SELECT title
FROM movie
WHERE id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 1
)
AND id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 2
);
INSERT INTO actor (name, birth_date)
VALUES 
('Actor 1', '1990-01-01'),
('Actor 2', '1992-02-02');

INSERT INTO movie (title, release_year, duration, production_id, director_id)
VALUES
('Test Movie 1', 2020, '02:00:00', 1, 1),
('Test Movie 2', 2021, '01:50:00', 1, 1);

INSERT INTO movie_actor (movie_id, actor_id, role)
VALUES
(6, 4, 'Hero'),
(6, 5, 'Friend'),
(7, 4, 'Police');
SELECT title
FROM movie
WHERE id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 4
)
AND id IN (
    SELECT movie_id
    FROM movie_actor
    WHERE actor_id = 5
);
-- =========================
-- TEST DATA FOR ALL QUERIES
-- =========================

-- Production
INSERT INTO production (id, name, address)
VALUES
(1, 'Warner Bros', 'USA'),
(2, 'Marvel Studios', 'USA'),
(3, 'Studio Canal', 'France');

-- Directors
INSERT INTO director (id, name, birth_date)
VALUES
(1, 'Christopher Nolan', '1970-07-30'),
(2, 'James Cameron', '1954-08-16');

-- Actors
INSERT INTO actor (id, name, birth_date)
VALUES
(1, 'Keanu Reeves', '1964-09-02'),
(2, 'Leonardo DiCaprio', '1974-11-11'),
(3, 'Brad Pitt', '1963-12-18'),
(4, 'Tom Cruise', '1962-07-03');

-- Movies
INSERT INTO movie (id, title, release_year, duration, production_id, director_id)
VALUES
(1, 'Matrix', 1999, '02:10:00', 1, 1),
(2, 'Inception', 2010, '02:28:00', 1, 1),
(3, 'Titanic', 2014, '03:14:00', 2, 2),
(4, 'Avatar', 2014, '02:40:00', 2, 2),
(5, 'Gladiator', 2000, '02:35:00', 3, 1),
(6, 'Empty Genre Movie', 2022, '01:30:00', 1, 1);

-- Movie Types
INSERT INTO movie_type (id, name_type)
VALUES
(1, 'Action'),
(2, 'Sci-Fi'),
(3, 'Drama');

-- Movie Genres
INSERT INTO movie_movie_type (movie_id, type_id)
VALUES
(1, 2),
(2, 2),
(3, 3),
(4, 2),
(5, 1);

-- Movie Actors
INSERT INTO movie_actor (movie_id, actor_id, role)
VALUES
(1, 1, 'Neo'),
(2, 2, 'Cobb'),
(2, 3, 'Friend'),
(5, 2, 'Hero'),
(5, 3, 'Warrior');
#----------------------------
SELECT 
    COUNT(*) AS total_movie,
    SUM(duration) AS total_duration,
    AVG(duration) AS avg_duration,
    MIN(duration) AS min_duration,
    MAX(duration) AS max_duration
FROM movie;
#----------------------------
SELECT production_id, COUNT(id)
FROM movie
GROUP BY production_id;
#----------------------------

SELECT release_year, COUNT(*)
FROM movie
GROUP BY release_year;
#----------------------------
SELECT director_id, COUNT(*)
FROM movie
GROUP BY director_id;

#---------------------------
SELECT actor_id, COUNT(movie_id)
FROM movie_actor
GROUP BY actor_id;

SELECT actor_name, COUNT(movie_id)
FROM movie_actor
GROUP BY actor_name;

SELECT actor_id, COUNT(movie_id)
FROM movie_actor
GROUP BY actor_id
HAVING COUNT(movie_id) > 1;

SELECT actor_id, COUNT(movie_id) AS total_movies
FROM movie_actor
GROUP BY actor_id
ORDER BY total_movies DESC;

SELECT release_year, AVG(duration)
FROM movie
GROUP BY release_year
HAVING AVG(duration) > '02:30:00';

SELECT release_year, AVG(duration)
FROM movie
GROUP BY release_year;
#-------------------------------
SELECT release_year, AVG(duration)
FROM movie
WHERE release_year > 2000
GROUP BY release_year
HAVING AVG(duration) > '02:30:00';

SELECT release_year, AVG(duration)
FROM movie
GROUP BY release_year
HAVING AVG(duration) > '02:30:00' and release_year > 2000;
#---------------------------------
SELECT 
movie.title,
production.name AS production_name,
production.address
FROM movie
INNER JOIN production
ON movie.production_id = production.id;

SELECT 
m.title,
p.name AS production_name,
p.address
FROM movie m
INNER JOIN production p
ON m.production_id = p.id;

SELECT 
p.id AS movienum,
p.name,
m.title
FROM production p
INNER JOIN movie m
ON p.id = m.production_id;

#-------------------
#6List movie titles and production company names for movies released on or after 2014
SELECT 
m.title,
p.name AS production_name
FROM movie m
INNER JOIN production p
ON m.production_id = p.id
WHERE m.release_year >= 2014;

#1
SELECT 
a.name,
COUNT(ma.movie_id) AS total_movies
FROM actor a
INNER JOIN movie_actor ma
ON a.id = ma.actor_id
GROUP BY a.name;

#2
SELECT 
m.title,
COUNT(ma.actor_id) AS total_actors
FROM movie m
INNER JOIN movie_actor ma
ON m.id = ma.movie_id
GROUP BY m.title;

#3
SELECT 
    p.name,
    m.title,
    m.duration
FROM production p
INNER JOIN movie m
ON p.id = m.production_id
WHERE m.duration > '02:30:00';

#4
SELECT 
a.name,
COUNT(q.id) AS total_quotes
FROM actor a
INNER JOIN quote q
ON a.id = q.actor_id
GROUP BY a.name;

#5
SELECT 
m.title,
COUNT(q.id) AS total_quotes
FROM movie m
INNER JOIN quote q
ON m.id = q.movie_id
GROUP BY m.title;

#7
SELECT 
p.name,
AVG(m.duration) AS avg_duration
FROM production p
INNER JOIN movie m
ON p.id = m.production_id
GROUP BY p.name
having ;

#8
SELECT 
m.title,
p.name AS production_name
FROM movie m
INNER JOIN production p
ON m.production_id = p.id
WHERE p.address LIKE '%USA%';

#9
SELECT 
a.name,
m.title
FROM actor a
INNER JOIN movie_actor ma
ON a.id = ma.actor_id
INNER JOIN movie m
ON ma.movie_id = m.id
WHERE ma.role IS NOT NULL;
USE new_database;
--------------------------------------
#m-m inner join
SELECT 
a.name AS actor_name,m.title AS movie_title,q.text AS movie_quote
FROM actor a
INNER JOIN quote q
ON a.id = q.actor_id
INNER JOIN movie m
ON m.id = q.movie_id;
#use 4 table , 3 join 
SELECT 
m.title AS movie_title,
a.name AS actor_name,
q.text AS quote_text
FROM movie m
INNER JOIN quote q
ON m.id = q.movie_id
INNER JOIN actor a
ON a.id = q.actor_id
INNER JOIN movie_actor ma
ON ma.movie_id = m.id 
AND ma.actor_id = a.id;
----------------------------
#type using left join 
SELECT 
mt.name_type,m.title
FROM movie_type mt
LEFT JOIN movie_movie_type mmt
ON mt.id = mmt.type_id
LEFT JOIN movie m
ON m.id = mmt.movie_id;

SELECT 
mt.name_type,m.title
FROM movie_type mt
right JOIN movie_movie_type mmt
ON mt.id = mmt.type_id
right JOIN movie m
ON m.id = mmt.movie_id;
--------------------------
#LEFT JOIN Exercises:
#1. List all movies and their production company names, including movies that do not have a production company assigned.
SELECT 
m.title,p.name AS production_name
FROM movie m
LEFT JOIN production p
ON m.production_id = p.id;
#2. List all actors and the movies they acted in, including actors who have not acted in any movie.
SELECT 
a.name AS actor_name,m.title AS movie_title
FROM actor a
LEFT JOIN movie_actor ma
ON a.id = ma.actor_id
LEFT JOIN movie m
ON ma.movie_id = m.id;
------------------------------------
#rigth join 
#List all actors and the quotes they said using RIGHT JOIN, including quotes that are not linked to any actor.
SELECT 
a.name AS actor_name,q.text AS quote_text
FROM actor a
RIGHT JOIN quote q
ON a.id = q.actor_id;
#Display all movies and their genres using RIGHT JOIN, including genres that currently have no movies assigned
SELECT 
m.title AS movie_title,mt.name_type AS genre
FROM movie m
RIGHT JOIN movie_movie_type mmt
ON m.id = mmt.movie_id
RIGHT JOIN movie_type mt
ON mt.id = mmt.type_id;
--------------------------------
#union
SELECT name FROM actor
UNION
SELECT name FROM director;
----------------
#full
SELECT 
m.title AS movie_title,
mt.name_type AS genre
FROM movie m
LEFT JOIN movie_movie_type mmt
ON m.id = mmt.movie_id
LEFT JOIN movie_type mt
ON mt.id = mmt.type_id
UNION
SELECT 
m.title AS movie_title,
mt.name_type AS genre
FROM movie m
RIGHT JOIN movie_movie_type mmt
ON m.id = mmt.movie_id
RIGHT JOIN movie_type mt
ON mt.id = mmt.type_id;
----------------
#crossjoin
SELECT 
a.name AS actor_name,
m.title AS movie_title
FROM actor a
CROSS JOIN movie m;
USE new_database;
-------------------
CREATE INDEX idx_movie_title
ON movie(title);
---------------------
#using veiw 
CREATE VIEW long_movies AS
SELECT 
id,
title,
release_year,
duration
FROM movie
WHERE duration > '02:30:00';
SELECT * FROM long_movies;
--------------------
#update
UPDATE long_movies
SET release_year = 2020
WHERE id = 2;
SELECT * FROM long_movies;
--------------------------
#
CREATE VIEW movie_actor_view AS
SELECT 
m.title AS movie_title,
a.name AS actor_name,
ma.role
FROM movie m
INNER JOIN movie_actor ma
ON m.id = ma.movie_id
INNER JOIN actor a
ON a.id = ma.actor_id;
SELECT * FROM movie_actor_view;
--------------------




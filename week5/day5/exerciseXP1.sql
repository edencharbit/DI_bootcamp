---1---
-- SELECT name FROM language

---2---
-- SELECT film.title, film.description, language.name 
-- FROM film
-- INNER JOIN language 
-- ON film.language_id = language.language_id

---3---
-- SELECT film.title, film.description, language.name 
-- FROM language
-- LEFT JOIN film 
-- ON film.language_id = language.language_id

---4---
-- CREATE TABLE new_film(
-- id SERIAL PRIMARY KEY,
-- name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES
-- ('Inception'),
-- ('Interstellar'), 
-- ('The Holiday');

-- SELECT * FROM new_film

---5---
-- CREATE TABLE customer_review(
-- review_id SERIAL PRIMARY KEY, 
-- title VARCHAR(50) NOT NULL, 
-- film_id INTEGER, 
-- language_id INTEGER,
-- score INT NOT NULL, 
-- review_text VARCHAR(255) NOT NULL, 
-- last_update DATE NOT NULL,
-- FOREIGN KEY(film_id) REFERENCES new_film(id) ON DELETE CASCADE,
-- FOREIGN KEY (language_id) REFERENCES language(language_id)
-- )

---6---
-- INSERT INTO customer_review (film_id, title, language_id, score, review_text, last_update) VALUES
-- ((SELECT id FROM new_film WHERE name = 'Inception'), 'Inception', (SELECT language_id FROM language WHERE name = 'English'), 10, 'Incredible', '01/01/2018'), 
-- ((SELECT id FROM new_film WHERE name = 'The Holiday'), 'The Holiday', (SELECT language_id FROM language WHERE name = 'English'), 9, 'Very beautiful movie', '01/09/2013')

-- SELECT * FROM customer_review

---7---
-- DELETE FROM new_film WHERE id = 1;
------NO PROBLEM TO DELETE BESAUSE OF "ON DELETE CASCADE" SO IT WAS DELETED SUCCESSFULLY

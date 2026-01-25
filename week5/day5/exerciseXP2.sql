---1---
-- UPDATE film 
-- SET language_id = (SELECT language_id FROM language WHERE name = 'French')
-- WHERE title LIKE 'A%'

-- SELECT film.title, film.language_id, language.language_id, language.name
-- FROM film 
-- LEFT JOIN language 
-- ON film.language_id= language.language_id

---2---
---fk : store_id, address_id 

---3---
-- DROP TABLE customer_review;

---4---
-- SELECT COUNT(*) 
-- FROM rental 
-- WHERE return_date IS NULL;

---5---
-- SELECT film.title, film.rental_rate 
-- FROM film
-- INNER JOIN inventory ON film.film_id = inventory.film_id
-- INNER JOIN rental ON rental.inventory_id = inventory.inventory_id 
-- WHERE rental.return_date IS NULL
-- ORDER BY film.rental_rate DESC LIMIT 30

---6---
-- SELECT film.title 
-- FROM film 
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE film.description ILIKE '%sumo%' 
-- AND actor.first_name = 'Penelope' AND actor.last_name = 'Monroe';
-- ---THE FIST FILM : Park Citizen

-- SELECT film.title 
-- FROM film
-- INNER JOIN film_category ON film_category.film_id = film.film_id
-- INNER JOIN category ON category.category_id = film_category.category_id
-- WHERE category.name = 'Documentary'
-- AND film.length < 60 
-- AND film.rating = 'R'
-- --- THE SECOND FILM : Cupboard Sinners

-- SELECT f.title
-- FROM film f
-- JOIN inventory i ON f.film_id = i.film_id
-- JOIN rental r ON i.inventory_id = r.inventory_id
-- JOIN customer cu ON r.customer_id = cu.customer_id
-- JOIN payment p ON r.rental_id = p.rental_id
-- WHERE cu.first_name = 'Matthew' AND cu.last_name = 'Mahan'
-- AND p.amount > 4.00
-- AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';
-- ---THE THIRD FILM : Sugar Wonka

SELECT f.title, f.description, f.replacement_cost
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN customer cu ON r.customer_id = cu.customer_id
WHERE cu.first_name = 'Matthew' AND cu.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;
---THE FOURTH FILM : Stone Fire




-- 1. Création de la table temporaire pour les athlètes de deux sports
CREATE TEMPORARY TABLE two_sport_medalists AS
SELECT 
    p.id AS person_id,
    p.full_name,
    COUNT(DISTINCT s.id) AS unique_sports,
    COUNT(ce.medal_id) AS total_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN event e ON ce.event_id = e.id
JOIN sport s ON e.sport_id = s.id
WHERE ce.medal_id IS NOT NULL
GROUP BY p.id, p.full_name
HAVING unique_sports = 2;

-- 2. Identification des 3 meilleurs compétiteurs
SELECT *
FROM two_sport_medalists
WHERE person_id IN (
    SELECT person_id 
    FROM two_sport_medalists
    ORDER BY total_medals DESC
    LIMIT 3
);
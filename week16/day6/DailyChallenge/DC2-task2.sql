-- 1. Création de la table temporaire
CREATE TEMPORARY TABLE persistent_non_medalists AS
SELECT 
    p.full_name, 
    COUNT(DISTINCT gc.games_id) AS games_count
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
WHERE p.id NOT IN (
    -- Sous-requête pour exclure tous ceux qui ont au moins une médaille
    SELECT DISTINCT gc2.person_id
    FROM games_competitor gc2
    JOIN competitor_event ce ON gc2.id = ce.competitor_id
    WHERE ce.medal_id IS NOT NULL
)
GROUP BY p.id, p.full_name
HAVING games_count > 3;

-- 2. Affichage du contenu
SELECT full_name, games_count
FROM persistent_non_medalists
ORDER BY games_count DESC;
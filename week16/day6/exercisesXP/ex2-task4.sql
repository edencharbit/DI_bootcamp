CREATE TEMPORARY TABLE seasonal_cross_participants AS
SELECT p.id, p.full_name
FROM person p
WHERE EXISTS (
    -- Sous-requête pour l'été
    SELECT 1 FROM games_competitor gc
    JOIN games g ON gc.games_id = g.id
    WHERE gc.person_id = p.id AND g.season = 'Summer'
)
AND EXISTS (
    -- Sous-requête pour l'hiver
    SELECT 1 FROM games_competitor gc
    JOIN games g ON gc.games_id = g.id
    WHERE gc.person_id = p.id AND g.season = 'Winter'
);

-- Pour vérifier la liste :
SELECT * FROM seasonal_cross_participants;
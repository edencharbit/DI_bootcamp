CREATE TEMPORARY TABLE dual_season_medalists AS
SELECT 
    p.id AS person_id,
    p.full_name,
    SUM(CASE WHEN g.season = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN g.season = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN games g ON gc.games_id = g.id
JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id IS NOT NULL
GROUP BY p.id, p.full_name
HAVING summer_medals > 0 AND winter_medals > 0;

-- Affichage des résultats
SELECT * FROM dual_season_medalists;
SELECT 
    nr.region_name,
    AVG(medal_count) AS avg_medals_region
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN (
    SELECT gc.person_id, COUNT(ce.medal_id) AS medal_count
    FROM games_competitor gc
    LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id
) AS p_medals ON pr.person_id = p_medals.person_id
GROUP BY nr.region_name
HAVING AVG(medal_count) > (
    -- Sous-requête pour la moyenne globale
    SELECT COUNT(medal_id) * 1.0 / COUNT(DISTINCT person_id)
    FROM games_competitor gc
    LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id
);
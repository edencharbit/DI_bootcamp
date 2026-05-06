SELECT 
    nr.region_name, 
    SUM(max_medals_per_event.medal_count) AS total_medals
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN (
    -- Sous-requête pour trouver le max de médailles par événement par compétiteur
    SELECT 
        gc.person_id, 
        MAX(event_counts.medals) AS medal_count
    FROM games_competitor gc
    JOIN (
        SELECT competitor_id, event_id, COUNT(medal_id) AS medals
        FROM competitor_event
        WHERE medal_id IS NOT NULL
        GROUP BY competitor_id, event_id
    ) AS event_counts ON gc.id = event_counts.competitor_id
    GROUP BY gc.person_id
) AS max_medals_per_event ON pr.person_id = max_medals_per_event.person_id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5;
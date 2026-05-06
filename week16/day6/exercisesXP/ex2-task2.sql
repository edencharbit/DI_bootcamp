CREATE TEMPORARY TABLE multiple_event_participation AS
SELECT 
    p.full_name, 
    gc.games_id, 
    count_events.total_events
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
JOIN (
    -- Sous-requête imbriquée pour filtrer les participations multiples
    SELECT competitor_id, COUNT(event_id) AS total_events
    FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(event_id) > 1
) AS count_events ON gc.id = count_events.competitor_id;
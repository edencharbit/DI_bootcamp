SELECT 
    nr.region_name, 
    COUNT(DISTINCT p.id) AS unique_competitors
FROM noc_region nr
JOIN person_region pr ON nr.id = pr.region_id
JOIN person p ON pr.person_id = p.id
WHERE p.id IN (
    -- Nested subquery to find competitors in > 3 events
    SELECT gc.person_id
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id
    HAVING COUNT(DISTINCT ce.event_id) > 3
)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5;
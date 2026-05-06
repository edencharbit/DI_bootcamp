SELECT 
    m.medal_name,
    (
        SELECT AVG(gc.age)
        FROM games_competitor gc
        JOIN competitor_event ce ON gc.id = ce.competitor_id
        WHERE ce.medal_id = m.id
    ) AS average_age
FROM medal m
WHERE m.id IN (
    SELECT DISTINCT medal_id 
    FROM competitor_event 
    WHERE medal_id IS NOT NULL
);


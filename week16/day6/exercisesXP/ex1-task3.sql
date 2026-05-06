CREATE TEMPORARY TABLE high_achievers AS
SELECT 
    p.full_name, 
    medal_counts.total_medals
FROM person p
JOIN (
    -- Subquery to aggregate medals per person
    SELECT gc.person_id, COUNT(ce.medal_id) AS total_medals
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    WHERE ce.medal_id IS NOT NULL
    GROUP BY gc.person_id
) AS medal_counts ON p.id = medal_counts.person_id
WHERE medal_counts.total_medals > 2;

-- To view the results:
SELECT * FROM high_achievers;
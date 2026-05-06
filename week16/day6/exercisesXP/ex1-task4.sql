CREATE TEMPORARY TABLE temp_competitor_analysis AS
SELECT 
    p.id AS person_id, 
    p.full_name
FROM person p;

DELETE FROM temp_competitor_analysis
WHERE person_id NOT IN (
    -- Subquery identifying anyone who has won a medal
    SELECT DISTINCT gc.person_id
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    WHERE ce.medal_id IS NOT NULL
);
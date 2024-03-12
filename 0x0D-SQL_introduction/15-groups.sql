-- List the number of records with same score
-- in the table `second_table` of the db

SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;

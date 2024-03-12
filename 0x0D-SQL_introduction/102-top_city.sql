-- display average temperature of 3 selcted cities
-- group by months July and August
-- and order by temperature in descending order

SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

-- show average temperature grouped by city
-- ordered by temperature in descending order

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

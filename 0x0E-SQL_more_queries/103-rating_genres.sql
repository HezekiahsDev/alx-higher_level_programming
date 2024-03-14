--List genres by ratings thier ratings

SELECT g.name AS genre_name, SUM(r.rate) AS rating_sum
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
INNER JOIN tv_show_ratings r ON sg.show_id = r.show_id
GROUP BY g.name
ORDER BY rating_sum DESC;

-- lists all genres
SELECT g.name AS 'genre', COUNT(s.genre_id) AS 'number_of_shows' FROM tv_genres AS g INNER JOIN tv_show_genres AS s ON g.id=s.genre_id GROUP BY g.name ORDER BY COUNT(g.name) DESC;

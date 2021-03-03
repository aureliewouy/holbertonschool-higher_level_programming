-- Lists show by their rating
SELECT g.name, SUM(r.rate) AS 'rating' FROM tv_genres AS g INNER JOIN tv_show_genres AS sg ON sg.genre_id=g.id INNER JOIN tv_shows AS s ON sg.show_id=s.id INNER JOIN tv_show_ratings AS r ON r.show_id=s.id GROUP BY g.name ORDER BY SUM(r.rate) DESC;

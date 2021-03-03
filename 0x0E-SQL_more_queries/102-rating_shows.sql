-- Lists show by their rating
SELECT s.title, SUM(r.rate) AS 'rating' FROM tv_shows AS s INNER JOIN tv_show_ratings AS r ON r.show_id=s.id GROUP BY s.title ORDER BY SUM(r.rate) DESC;

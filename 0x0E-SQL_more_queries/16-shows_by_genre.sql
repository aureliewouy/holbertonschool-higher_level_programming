-- Lists all shows and all genres link to that show
SELECT s.title, g.name FROM tv_shows AS s LEFT JOIN tv_show_genres AS sg ON sg.show_id=s.id LEFT JOIN  tv_genres AS g ON sg.genre_id=g.id ORDER BY s.title, g.name ASC;

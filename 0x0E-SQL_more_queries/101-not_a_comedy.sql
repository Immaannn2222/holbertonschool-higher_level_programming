-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (SELECT show_id
FROM tv_show_genres
JOIN tv_genres 
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy')
GROUP BY tv_shows.title
ORDER BY tv_shows.title;
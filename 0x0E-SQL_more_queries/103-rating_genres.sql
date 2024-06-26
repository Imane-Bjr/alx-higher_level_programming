-- Script that lists genres by their rating
SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating -- Query to join tables
FROM tv_genres
JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
     ON tv_show_genres.show_id = tv_shows.id
ORDER BY rating DESC;

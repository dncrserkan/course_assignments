-- write a SQL query to list the titles of all movies in which both Bradley Cooper and Jennifer Lawrence starred

SELECT title FROM movies WHERE id IN
    (SELECT movie_id FROM stars WHERE person_id IN
         (SELECT id FROM people WHERE name IN ('Jennifer Lawrence', 'Bradley Cooper'))
    GROUP BY movie_id
    HAVING COUNT(DISTINCT person_id) = 2
    );

-- number of columns: 1
-- number of rows: 4
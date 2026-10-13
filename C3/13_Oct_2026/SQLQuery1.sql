CREATE DATABASE CaseStudy;
USE CaseStudy;
SELECT name FROM sys.tables ORDER BY name;
-- Fetch all the painting which are not displayed on any musium

SELECT *FROM work WHERE museum_id is not null;
SELECT *FROM work WHERE museum_id =67 AND artist_id between 500 and 700;

-- identify the musium with invalid city information in the data set
SELECT * FROM museum
WHERE city LIKE '[0-9]%';

-- identify the museum which are open on both Sunday and Monday



--indentify the top 5 populer artist [based on moste number of painting in a museum
 SELECT m.name AS museum,m.city,m.country,x.no_of_paintings
FROM (SELECT w.museum_id,COUNT(*) AS no_of_paintings,RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
    FROM work w
    WHERE w.museum_id IS NOT NULL

    GROUP BY w.museum_id
) AS x
JOIN museum AS m ON m.museum_id = x.museum_id
WHERE x.rnk <= 5
ORDER BY x.no_of_paintings DESC;
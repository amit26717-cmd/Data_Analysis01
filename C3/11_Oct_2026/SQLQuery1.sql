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


-- 1. Total number of titles
SELECT COUNT(*) AS total_titles
FROM netflix_titles;

-- 2. Count of Movies vs TV Shows
SELECT type, COUNT(*) AS count
FROM netflix_titles
GROUP BY type;

-- 3. Top 10 countries with most content
SELECT country, COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

-- 4. Titles released after 2015
SELECT title, release_year, type
FROM netflix_titles
WHERE release_year > 2015
ORDER BY release_year DESC;

-- 5. Most common ratings
SELECT rating, COUNT(*) AS count
FROM netflix_titles
GROUP BY rating
ORDER BY count DESC;

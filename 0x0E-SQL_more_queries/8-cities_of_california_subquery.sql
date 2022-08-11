-- script that lists all the cities of California
USE hbtn_0d_usa;
SELECT name, id FROM cities 
WHERE name = 'California'
ORDER BY cities.id ASC;

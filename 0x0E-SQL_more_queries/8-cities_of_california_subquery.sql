-- script that lists all the cities of California
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id, name) VALUES(California);
SELECT California FROM cities ORDER BY ASC;

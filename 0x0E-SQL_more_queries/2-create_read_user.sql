-- script that creates the database hbtn_0d_2 and the user user_0d_2

-- craete the database
CREATE DATABASE IF EXISTS hbtn_0d_2;

-- create the user
CREATE USER IF NOT EXISTS user_0d_2;

-- grant the permission
GRANT SELECT ON hbtn_0d_2 ON TO user_0d_2@localhost;

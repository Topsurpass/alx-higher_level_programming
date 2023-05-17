-- Creates the database hbtn_0d_2 and the user user_0d_2.
-- If the above exists, script should not fail.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2.
-- user_0d_2 password should be set to user_0d_2_pwd.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Login to server, see all databases and tables but user cannot perform
-- any task on them i.e Minimal Access.
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

-- User can execute only SELECT(print rows) on tables within this database only.
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

-- Creates the MySQL server user user_0d_1.
-- The user showl have all privileges on my MySQL server.
-- User password should be user_0d_1_pwd.
-- If user already exists, script should not fail.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;

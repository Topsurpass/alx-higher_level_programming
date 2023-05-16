-- Creates a table called first_table in the current database
-- in my MySQL server. Database name will be passed as argument
-- from the command line.
-- The table below has 2 columns, id (an integer) and name (a sting)

CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
);

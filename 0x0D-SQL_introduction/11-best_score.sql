-- List all records with a score >= 10 in the table second_table of
-- the database hbtn_0c_0 in my MySQL server. Display both score and
-- name in descending order.

SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;

#!/usr/bin/python3

"""
This module lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    """Connect to mysql server"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    """Create a cursor"""
    cur = db.cursor()

    """Execute the SQL query and save output in a turple"""
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states
    ON states.id = cities.state_id
    ORDER BY id ASC""")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()

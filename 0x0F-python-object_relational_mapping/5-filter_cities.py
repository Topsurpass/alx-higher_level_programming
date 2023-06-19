#!/usr/bin/python3

"""
This module takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa

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

    state = argv[4]
    """Create a cursor"""
    cur = db.cursor()

    """Execute the SQL query and save output in a turple"""

    query = """SELECT cities.name
            FROM states
            INNER JOIN cities
            ON states.id = cities.state_id
            WHERE states.name LIKE %s
            ORDER BY cities.id ASC"""
    cur.execute(query, (state,))

    rows = cur.fetchall()
    print(', '.join([str(row[0]) for row in rows]))

    cur.close()
    db.close()

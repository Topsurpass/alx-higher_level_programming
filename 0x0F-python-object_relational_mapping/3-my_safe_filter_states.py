#!/usr/bin/python3

"""
This module takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
N.B: Query must be safe from MYSQL injections

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    """Connect to database @argv[3] using localhost and port 3306"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    state = argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """Another method
    query = 'SELECT * FROM states WHERE name=%s ORDER BY
                 id ASC'
    rows = cur.execute(query, (argv[4], ))
    """

    """Save all table's rows and return rows turple"""
    rows = cur.fetchall()
    for row in rows:
        if state in row:
            print(row)
    cur.close()
    db.close()

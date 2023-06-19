#!/usr/bin/python3

"""
This module contains a script that lists all states from the database
hbtn_0e_0_usa

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
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """Save all table's rows and return rows turple"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

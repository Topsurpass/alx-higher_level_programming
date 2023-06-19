#!/usr/bin/python3

"""
This module lists all states with a name starting with N (upper N)
from the database hbtn_2e_0_usa

"""

import MySQLdb
from sys import argv

"""If module is exported do not execute code"""
if __name__ == '__main__':

    """Connect to the database with localhost and port 3306"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    """Save all table rows in rows turple"""
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()

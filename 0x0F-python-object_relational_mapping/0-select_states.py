#!/usr/bin/python3
""" Lists all the states from a database hbtn_0e_0_usa
mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    row = cursor.fetchall()
    for states in row:
        print(states)
    cursor.close()
    db.close()

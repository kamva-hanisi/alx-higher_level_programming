#!/usr/bin/python3
""" Displays all values in the states table of hbtn_0e_0_usa
    in a safe from MySQL injections
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
    cursor.execute("SELECT * FROM states WHERE name LIKE = %s", (argv[4], ))
    row = cursor.fetchall()
    for state in row:
        print(state)
    cursor.close()
    db.close()

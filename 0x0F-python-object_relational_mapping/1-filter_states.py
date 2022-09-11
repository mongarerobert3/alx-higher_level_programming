#!/usr/bin/python3

"""Script to list all stattes from hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cur = connection.cursor()
    cur.execute("SELECT * FROM states WHERE name like BINARY 'N%'")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    connection.close()

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
    cur.execute("SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id;", (argv[4], ))
    query_rows = cur.fetchall()

    cities = []
    temp = 0
    for city in query_rows:
        cities.append(query_rows[temp][0])
        temp = temp + 1
    final_cities = ', '.join(cities)
    print(final_cities)
    cur.close()
    connection.close()

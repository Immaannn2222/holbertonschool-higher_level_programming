#!/usr/bin/python3
"""Module"""

import MySQLdb
from sys import argv
if __name__ == '__main__':
    """main func"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id=states.id\
                WHERE states.name = %s", (argv[4],))
    query = cur.fetchall()
    my_list = []
    for x in query:
        my_list.append(x[0])
    print(", ".join(my_list))
    cur.close()
    conn.close()

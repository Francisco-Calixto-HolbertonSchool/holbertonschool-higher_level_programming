#!/usr/bin/python3
'''takes name of state as argument and lists cities of that state'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
    sql = "SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE name = %s"
    cursor.execute(sql, (argv[4],))
    res = cursor.fetchall()
    for row in res:
        print(row)
    db.close()

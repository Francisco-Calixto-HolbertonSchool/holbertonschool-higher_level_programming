#!/usr/bin/python3
'''all values of states table (hbtn_0e_0_usa) that name matches argument'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
    sql = f'SELECT * FROM states ORDER BY id WHERE name IS {argv[4]}'
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        print(row)
    db.close()

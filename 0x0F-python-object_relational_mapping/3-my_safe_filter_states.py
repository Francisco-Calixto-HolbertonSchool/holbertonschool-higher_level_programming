#!/usr/bin/python3
'''all values of states table (hbtn_0e_0_usa) that name matches argument'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
<<<<<<< HEAD
    sql = "SELECT * FROM states ORDER BY id WHERE Name = %s;", argv[2]
=======
    sql = f'SELECT * FROM states ORDER BY id WHERE Name = {argv[2]};'
>>>>>>> c2664f729c43aac03b029eb5668af253a574a67a
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        if row[1] == argv[4]:
            print(row)
    db.close()

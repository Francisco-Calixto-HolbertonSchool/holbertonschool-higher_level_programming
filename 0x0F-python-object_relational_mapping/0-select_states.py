#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
    sql = "SELECT * FROM states ORDER BY id"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()

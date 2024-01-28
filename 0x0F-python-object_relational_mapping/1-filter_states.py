#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a name
starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]

    connection = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        host='localhost',
        database=db_name,
        port=3306
    )

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * \
                       FROM states\
                       WHERE name LIKE 'N%'\
                       ORDER BY id ASC")

        result = cursor.fetchall()
        for row in result:
            if row[1][0] == 'N':
                print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()

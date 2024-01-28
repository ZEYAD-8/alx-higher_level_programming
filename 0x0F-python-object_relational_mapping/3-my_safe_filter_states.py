#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa with a
given name and is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_searched = argv[4]

    connection = MySQLdb.connect(
        user=mysql_username,
        passwd=mysql_password,
        host='localhost',
        database=db_name,
        port=3306
    )

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT *\
                       FROM states\
                       WHERE name='{:s}'\
                       ORDER BY id ASC".format(state_searched))

        result = cursor.fetchall()
        for row in result:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()

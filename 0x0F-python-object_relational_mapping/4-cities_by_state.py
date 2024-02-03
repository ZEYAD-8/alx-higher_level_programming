#!/usr/bin/python3
"""
python script that lists all cities from the database hbtn_0e_4_usa
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
        cursor.execute(
            "SELECT cities.id, cities.name, cities.state_id\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC")

        result = cursor.fetchall()
        for row in result:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()

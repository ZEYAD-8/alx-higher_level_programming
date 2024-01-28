#!/usr/bin/python3
"""
python script that lists all cities from the database hbtn_0e_4_usa
with specified state name
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

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
            "SELECT cities.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name LIKE %s\
            ORDER BY cities.id", (state_name,))

        result = cursor.fetchall()
        print(", ".join(city[0] for city in result))

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()

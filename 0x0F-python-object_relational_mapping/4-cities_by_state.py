#!/usr/bin/python3
"""Lists all cities from a database"""


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    if len(argv) == 4:
        db = MySQLdb.connect(user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             host="localhost",
                             port=3306)
        c = db.cursor()
        select = ("""SELECT cities.id, cities.name, states.name
        FROM cities LEFT JOIN states ON states.id=cities.state_id
        ORDER BY cities.id""")
        c.execute(select)
        for row in c:
            print("{}".format(row))
        c.close()
        db.close()

#!/usr/bin/python3
"""Lists all statess from a database"""


if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    if len(argv) == 5:
        db = MySQLdb.connect(user=argv[1],
                             passwd=argv[2],
                             db=argv[3],
                             host="localhost",
                             port=3306)
        c = db.cursor()
        select = ("""SELECT cities.name FROM cities LEFT JOIN states ON
        states.id=cities.state_id WHERE states.name=%s ORDER BY
        cities.id ASC""")
        c.execute(select, [argv[4]])
        datas = c.fetchall()
        join = ', '.join([data[0] for data in datas])
        print(join)
        c.close()
        db.close()

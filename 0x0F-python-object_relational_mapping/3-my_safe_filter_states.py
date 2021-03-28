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
        select = ("""SELECT * FROM states WHERE name=%s
        ORDER BY id ASC""")
        c.execute(select, [argv[4]])
        for row in c:
            print("{}".format(row))
        c.close()
        db.close()

#!/usr/bin/python3
"""Lists all statess from a database"""


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
        c.execute("""SELECT * FROM states ORDER BY id ASC""")
        for row in c:
            print("{}".format(row))
        c.close()
        db.close()

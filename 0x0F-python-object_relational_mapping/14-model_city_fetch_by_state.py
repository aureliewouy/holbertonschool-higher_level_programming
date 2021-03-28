#!/usr/bin/python3
"""Lists all cities from a database"""


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from model_city import City

    if len(argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2],
                                       argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        s = session.query(City, State).filter(City.state_id == State.id).all()
        for c, s in s:
            print('{}: ({}) {}'.format(s.name, c.id, c.name))
        session.close()

#!/usr/bin/python3
"""Lists all states from a database"""


if __name__ == "__main__":

    from sys import argv
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    if len(argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2],
                                       argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        searchA = session.query(State).filter(State.name.like('%a%')).all()
        for state in searchA:
            session.delete(state)
        session.commit()
        session.close()

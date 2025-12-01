from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

'''
    Main object which SQLAlchemy uses to communicate with database.
    So, this is not one connection, but a factory of connections and manager. 
    Later, when doing SessionLocal(), that session is using engine as source of connections.
'''
engine = create_engine(
    settings.db.database_uri(),
    future=True,  # Uses new SQLAlchemy 2.0 style
    echo=True  # True - echoes SQL queries in console
)

'''
    SessionLocal is a class, sessionmaker returns a Class which can create new Session objects
'''
SessionLocal = sessionmaker(
    bind=engine,  # All future sessions will use this engine
    autoflush=False,  # Does not send changes to the database automatically
    autocommit=False  # Commit is done manualy
)


def get_db():
    db = SessionLocal()  # Opening new DB session(connection)
    try:
        yield db
    finally:
        db.close()  # Once done, connection get's closed

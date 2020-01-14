from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://shankar2:shankarsr123@localhost:5432/learn',echo=True)
engine.connect()
#models.Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()



from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from . import db

Base = declarative_base()
Base.metadata.create_all(db.engine)

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    def __repr__(self):
        return f"<User id={self.id},name={self.name},fullname={self.fullname}"
    
    @classmethod
    def create(cls, **kw):
        obj = cls(**kw)
        db.session.add(obj)
        db.session.commit()
    @classmethod
    def get(cls,**kw):
        obj = cls(**kw)
        return db.session.query(obj)

from datetime import datetime
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date

class Item(Base):
    __tablename__ = 'items'
    name = Column(String(255), nullable=False, unique=True)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<Item name = {self.name} id={self.id}>"


class Persistent(object):
    #__tablename__ = "persistents"
    createdOn = Column(DateTime)
    createdBy = Column(Integer)
    lastModifiedOn = Column(DateTime)
    lastModifiedBy = Column(Integer)
    version = Column(Integer)
    effectiveFrom = Column(Date)
    isEnabled = Column(Boolean)
    id = Column(Integer, primary_key=True, unique=True)   

class Role(Persistent, Base):
    __tablename__ = "roles"
    name = Column(String(255), nullable=False)
    permissions = Column(ARRAY(Integer))
    tags = Column(ARRAY(String))
    

    def __repr__(self):
        return f"<Role name = {self.name}>"



'''
class User(Persistent):
    pass

class Permission(Persistent):
    pass
'''
from datetime import datetime
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY

class Item(Base):
    __tablename__ = 'items'
    name = Column(String(255), nullable=False, unique=True)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<Item name = {self.name} id={self.id}>"


class Persistent(Base):
    createdOn = Column(datetime)
    createdBy = Column(Integer)
    lastModifiedOn = Column(datetime)
    lastModifiedBy = Column(Integer)
    version = Column(Integer)
    effectiveFrom = Column(datetime)
    isEnabled = Column(Boolean)
    id = Column(Integer, primary_key=True, unique=True)


class Role(Persistent):
    __tablename__ = "roles"
    name = Column(String(255), nullable=False, unique=False)
    permissions = Column(ARRAY(Integer))
    tags = Column(ARRAY(String))


'''
class User(Persistent):
    pass

class Permission(Persistent):
    pass
'''
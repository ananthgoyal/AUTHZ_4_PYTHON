from datetime import datetime
from multiprocessing.dummy import Array
from src.database import Base
from sqlalchemy import String, Boolean, Integer, Column, ARRAY, DateTime, Date

class Item(Base):
    __tablename__ = 'items'
    name = Column(String(255), nullable=False, unique=True)
    id = Column(String(255), primary_key=True)

    def __repr__(self):
        return f"<Item name = {self.name} id={self.id}>"


class Persistent(object):
    createdOn = Column(DateTime)
    createdBy = Column(String, nullable=True)
    lastModifiedOn = Column(DateTime, nullable=True)
    lastModifiedBy = Column(String, nullable=True)
    version = Column(Integer)
    effectiveFrom = Column(Date, nullable=True)
    isEnabled = Column(Boolean)
    id = Column(String, primary_key=True, unique=True)

class Role(Persistent, Base):
    __tablename__ = "roles"
    name = Column(String(255), nullable=False)
    permissions = Column(ARRAY(Integer))
    tags = Column(ARRAY(String))
    

    def __repr__(self):
        return f"<Role name = {self.name}>"


class Permission(Persistent, Base):
    __tablename__ = "permissions"
    can_create = Column(Boolean)
    can_update = Column(Boolean)
    can_delete = Column(Boolean)
    can_read = Column(Boolean)
    can_read_all = Column(Boolean)
    can_assign = Column(Boolean)
    can_share = Column(Boolean)
    role = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Permission ID = {self.id}>"


class User(Persistent, Base):
    __tablename__ = "users"
    name = Column(String(255))
    dateOfBirth = Column(Date)
    roles = Column(ARRAY(Integer))

    def __repr__(self):
        return f"<User ID = {self.id}>"

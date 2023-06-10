from database import Base
from sqlalchemy import String, Boolean, Integer, Column

class Item(Base):
    __tablename__ = 'items'
    name = Column(String(255), nullable=False, unique=True)
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"<Item name = {self.name} id={self.id}>"

'''
class Persistent(Base):
    pass

class Role(Persistent):
    pass

class User(Persistent):
    pass

class Permission(Persistent):
    pass
'''
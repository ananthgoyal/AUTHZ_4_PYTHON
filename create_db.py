from database import Base, engine
from models import Item
from models import Role
from models import Permission

Base.metadata.create_all(engine)

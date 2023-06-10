from database import Base, engine
from models import Item
from models import Role


Base.metadata.create_all(engine)

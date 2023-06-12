from pydantic import BaseModel

class Item(BaseModel):
    name: str
    id: int

    class Config:
        orm_mode = True
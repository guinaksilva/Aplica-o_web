from pydantic import BaseModel


class PCBase(BaseModel):
    name: str
    description: str


class PCCreate(PCBase):
    pass

class PCUpdate(PCBase):
    pass

class PC(PCBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

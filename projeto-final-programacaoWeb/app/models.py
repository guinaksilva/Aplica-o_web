from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class PC(Base):
    __tablename__ = "pcs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    is_active = Column(Boolean, default=True)

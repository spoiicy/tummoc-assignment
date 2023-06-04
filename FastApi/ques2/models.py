from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(20))
    full_name = Column(String(20))
    email = Column(String)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
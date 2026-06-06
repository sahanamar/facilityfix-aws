# from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Column, Integer, String
from app.database import Base
from app.enums.enums import UserRole


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    role = Column(SQLEnum(UserRole), nullable=False)
    password_hash = Column(String(255),nullable=False)
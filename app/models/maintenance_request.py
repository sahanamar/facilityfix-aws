# from enum import Enum
from urllib.request import Request
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from app.database import Base
from app.enums.enums import Priority, RequestStatus


class MaintenanceRequest(Base):
    __tablename__ = "maintenance_requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    priority = Column(SQLEnum(Priority), nullable=False)
    status = Column(SQLEnum(RequestStatus), nullable=False)
    created_at = Column(DateTime, default=datetime)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    technician_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )
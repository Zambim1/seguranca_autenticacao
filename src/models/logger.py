from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship


class Log(Base):
    __tablename__: "logs"

    log_id = Column(Integer, rimary_key=True, autoincreement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_ip = Column(String)
    
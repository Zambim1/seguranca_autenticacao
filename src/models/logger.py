from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from src.database import Base

class Log(Base):
    __tablename__ = "logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_ip = Column(String)

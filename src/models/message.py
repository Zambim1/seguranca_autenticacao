from sqlalchemy import Column, Integer, ForeignKey, LargeBinary, DateTime
from base64 import b64encode
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base

#  MODELO ORM (SQLAlchemy)
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))

    encrypted_message = Column(LargeBinary, nullable=False)
    encrypted_key = Column(LargeBinary, nullable=False)
    nonce = Column(LargeBinary, nullable=False)
    tag = Column(LargeBinary, nullable=False)

    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", foreign_keys=[sender_id], backref="sent_messages")
    receiver = relationship("User", foreign_keys=[receiver_id], backref="received_messages")


# SCHEMAS Pydantic 
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class MessageCreate(BaseModel):
    receiver_id: int = Field(..., description="ID of the user who will receive the message")
    message: str = Field(..., description="Plain text message to be encrypted")

class MessageResponse(BaseModel):
    sender_id: int
    encrypted_message: str
    encrypted_key: str
    nonce: str
    tag: str
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def model_validate(cls, obj):
        return cls(
            sender_id=obj.sender_id,
            encrypted_message=b64encode(obj.encrypted_message).decode(),
            encrypted_key=b64encode(obj.encrypted_key).decode(),
            nonce=b64encode(obj.nonce).decode(),
            tag=b64encode(obj.tag).decode(),
            timestamp=obj.timestamp,
        )
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

from src.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

# ORM Models
class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password_hash = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    public_key = Column(String)
    private_key = Column(String)  
    role = relationship("Role", back_populates="users")

# Pydantic Schemas
class UserBase(BaseModel):
    username: str = Field(..., description="Unique username")
    role: str = Field(..., description="Users role identifier")


class UserCreate(UserBase):
    password: str = Field(..., description="Password of user", repr=False)


class UserUpdate(BaseModel):
    id: int = Field(None, description="Unique user identifier")
    username: Optional[str] = Field(None, description="Unique username")


class RoleResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    username: str
    role: RoleResponse

    model_config = ConfigDict(from_attributes=True)
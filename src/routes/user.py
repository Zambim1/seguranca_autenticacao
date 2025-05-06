from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from src.models.user import UserCreate, UserUpdate, UserResponse
from src.services.user import create_user, get_user_list, update_user
from src.database import get_db 

router = APIRouter(prefix="/users", tags=["Users"])

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.models.user import UserCreate, UserUpdate, UserResponse
from src.services.user import (
    create_user,
    get_user_list,
    update_user,
)
from src.database import get_db 

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def post_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    return UserResponse.model_validate(user)

@router.get("/", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_users(db: Session = Depends(get_db)):
    users = get_user_list(db)
    return [UserResponse.model_validate(user) for user in users]

@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def put_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user_data)
    return UserResponse.model_validate(updated_user)


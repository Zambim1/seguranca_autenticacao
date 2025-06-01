from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import List
from Crypto.PublicKey import RSA

from src.models.user import User, UserCreate, UserUpdate
from src.utils.config import hash_password, get_role_by_name, get_object_by_id


def generate_rsa_key_pair() -> tuple[str, str]:
    key = RSA.generate(2048)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return public_key, private_key


def create_user(db: Session, user_data: UserCreate) -> User:
    existing = db.query(User).filter(User.username == user_data.username).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    role = get_role_by_name(db, user_data.role)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or non-existent role"
        )

    hashed = hash_password(user_data.password)
    public_key, private_key = generate_rsa_key_pair()

    new_user = User(
        username=user_data.username,
        password_hash=hashed,
        role_id=role.id,
        public_key=public_key,
        private_key=private_key
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Integrity error. Invalid data."
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while creating user."
        )


def get_user_list(db: Session) -> List[User]:
    return db.query(User).all()


def update_user(db: Session, user_id: int, new_user_data: UserUpdate) -> User:
    user = get_object_by_id(db, User, user_id)

    if new_user_data.username is not None:
        existing_user = db.query(User).filter(User.username == new_user_data.username).first()
        if existing_user and existing_user.id != user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        user.username = new_user_data.username

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while updating user"
        )

from sqlalchemy.orm import joinedload

def delete_user(db: Session, user_id: int) -> None:
    user = db.query(User).options(joinedload(User.role)).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.role.name == "Admin":
        db.delete(user)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while deleting user"
        )


    

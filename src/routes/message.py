from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.models.message import MessageCreate, MessageResponse
from src.services.message import send_encrypted_message, get_user_messages
from src.utils.config import get_current_user_username, get_user_by_username

router = APIRouter(prefix="/messages", tags=["Messages"])

# Enviar mensagem
@router.post("/", status_code=status.HTTP_200_OK)
def send_message(
    message_data: MessageCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_username)
):
    sender = get_user_by_username(db, current_user)
    if not sender:
        raise HTTPException(status_code=404, detail="Sender not found")

    send_encrypted_message(db, sender.id, message_data)

    return {"msg": "Message sent successfully"}

# Receber mensagens
@router.get("/", response_model=List[MessageResponse], status_code=status.HTTP_200_OK)
def receive_messages(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_username)
):
    user = get_user_by_username(db, current_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    messages = get_user_messages(db, user.id)
    return [MessageResponse.model_validate(m) for m in messages]
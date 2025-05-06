from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Depends
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

from src.models.message import Message
from src.models.user import User
from src.models.message import MessageCreate

def send_encrypted_message(db: Session, sender_id: int, message_data: MessageCreate) -> Message:
    # Busca o usuário destinatário
    receiver = db.query(User).filter(User.id == message_data.receiver_id).first()
    if not receiver:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Receiver not found"
        )

    # Criptografia AES da mensagem
    aes_key = get_random_bytes(16)
    aes_cipher = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = aes_cipher.encrypt_and_digest(message_data.message.encode())

    # Criptografia da chave AES com RSA pública do destinatário
    try:
        pub_key = RSA.import_key(receiver.public_key.encode())
        rsa_cipher = PKCS1_OAEP.new(pub_key)
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to encrypt AES key with receiver's public key"
        )

    # Armazena a mensagem criptografada
    message = Message(
        sender_id=sender_id,
        receiver_id=receiver.id,
        encrypted_message=ciphertext,
        encrypted_key=encrypted_aes_key,
        nonce=aes_cipher.nonce,
        tag=tag
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_user_messages(db: Session, user_id: int) -> list[Message]:
    return db.query(Message).filter(Message.receiver_id == user_id).order_by(Message.timestamp.desc()).all()
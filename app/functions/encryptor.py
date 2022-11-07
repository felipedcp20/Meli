from cryptography.fernet import Fernet
from fastapi import HTTPException


def encrypt(message, key):
    """
        Message (string): Message to Encrypt
        key (string): key to Encrypt String

    Returns:
        string: Message Encrypted
    """
    try:
        fernet = Fernet(key)
        encMessage = fernet.encrypt(message.encode())
        return encMessage
    except Exception as error:
        raise HTTPException(status_code=404, detail=error) from error


def decrypt(message, key):
    """
        Message (string): Message Encrypted
        key (string): key to decrypt String

    Returns:
        string: Message decrypted
    """
    try:
        fernet = Fernet(key)
        decMessage = fernet.decrypt(message).decode()
        return decMessage
    except Exception as error:
        raise HTTPException(status_code=404, detail=error) from error

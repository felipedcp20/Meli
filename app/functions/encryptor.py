from cryptography.fernet import Fernet


def encrypt(message, key):
    """
        Message (string): Message to Encrypt
        key (string): key to Encrypt String

    Returns:
        string: Message Encrypted
    """
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    return encMessage


def decrypt(message, key):
    """
        Message (string): Message Encrypted
        key (string): key to decrypt String

    Returns:
        string: Message decrypted
    """
    fernet = Fernet(key)
    decMessage = fernet.decrypt(message).decode()
    return decMessage

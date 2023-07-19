```python
from cryptography.fernet import Fernet

ENCRYPTED_DATA = {}

def generate_key():
    """
    Generate a key for encryption and decryption
    """
    return Fernet.generate_key()

def encrypt_data(data, key):
    """
    Encrypt the provided data using the provided key
    """
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """
    Decrypt the provided data using the provided key
    """
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def encrypt_data_handler(data):
    """
    Handle the process of data encryption
    """
    key = generate_key()
    encrypted_data = encrypt_data(data, key)
    ENCRYPTED_DATA['key'] = key
    ENCRYPTED_DATA['data'] = encrypted_data
    return ENCRYPTED_DATA

def decrypt_data_handler(encrypted_data, key):
    """
    Handle the process of data decryption
    """
    decrypted_data = decrypt_data(encrypted_data, key)
    return decrypted_data
```
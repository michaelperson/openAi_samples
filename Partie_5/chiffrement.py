from cryptography.fernet import Fernet
# Génération d'une clé (à stocker de manière sécurisée)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data: str) -> bytes:    
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data: bytes) -> str:    
    return cipher_suite.decrypt(encrypted_data).decode()

# Usage
sensitive_prompt = "Données sensibles..."
encrypted = encrypt_data(sensitive_prompt)
# Stocker 'encrypted' en base de données
#Plus tard, récupération
decrypted = decrypt_data(encrypted)




from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# Generar clau i IV (Initialization Vector)
key = os.urandom(32)  # Clau de 256 bits
iv = os.urandom(16)   # IV de 128 bits

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

plaintext = b"Missatge curt"  # Pot no ser múltiple de la mida del bloc
ciphertext = encryptor.update(plaintext) + encryptor.finalize()  # Pot ser incorrecte

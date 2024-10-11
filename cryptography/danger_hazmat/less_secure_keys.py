from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(16)  # Clau de mida incorrecta per AES-256
nonce = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
encryptor = cipher.encryptor()

plaintext = b"Missatge secret"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()  # Clau massa curta

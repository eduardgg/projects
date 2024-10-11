from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)  # Clau de 256 bits (reutilitzada)
iv = os.urandom(16)   # IV de 128 bits (reutilitzat)

cipher1 = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
cipher2 = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

encryptor1 = cipher1.encryptor()
encryptor2 = cipher2.encryptor()

plaintext1 = b"Missatge 1"
plaintext2 = b"Missatge 2"

ciphertext1 = encryptor1.update(plaintext1) + encryptor1.finalize()
ciphertext2 = encryptor2.update(plaintext2) + encryptor2.finalize()

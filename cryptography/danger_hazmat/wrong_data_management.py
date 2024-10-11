from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.urandom(32)
nonce = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
encryptor = cipher.encryptor()

plaintext = b"Missatge secret"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Manipulació incorrecta del ciphertext (afegint dades falses)
tampered_ciphertext = ciphertext + b"extra data"

decryptor = cipher.decryptor()
try:
    decrypted_text = decryptor.update(tampered_ciphertext) + decryptor.finalize()
except Exception as e:
    print("Error:", e)

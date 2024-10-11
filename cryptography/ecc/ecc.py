from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class ECC:
    def __init__(self):
        # Generate a new private key
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()
    
    def generate_keys(self):
        # Serialize private key to PEM format
        private_pem = self.private_key.private_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm = serialization.NoEncryption()
        )
        # Serialize public key to PEM format
        public_pem = self.public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_pem, public_pem

    def load_keys(self, private_pem, public_pem):
        # Load private key from PEM
        self.private_key = load_pem_private_key(private_pem, password=None)
        # Load public key from PEM
        self.public_key = load_pem_public_key(public_pem)

    def encrypt(self, plaintext):
        # Generate a shared key using ECDH
        shared_key = self.private_key.exchange(ec.ECDH(), self.public_key)
        
        # Derive a key for AES encryption
        derived_key = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = b'some_salt',
            iterations = 100000
        ).derive(shared_key)
        
        # Encrypt plaintext using AES
        cipher = Cipher(algorithms.AES(derived_key), modes.CTR(os.urandom(16)))
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
        
        return ciphertext, cipher.nonce

    def decrypt(self, ciphertext, nonce):
        # Generate a shared key using ECDH
        shared_key = self.private_key.exchange(ec.ECDH(), self.public_key)
        
        # Derive a key for AES encryption
        derived_key = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = b'some_salt',
            iterations = 100000
        ).derive(shared_key)
        
        # Decrypt ciphertext using AES
        cipher = Cipher(algorithms.AES(derived_key), modes.CTR(nonce))
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        
        return plaintext.decode()



import random
from sympy import isprime, mod_inverse
# Need to install sympy: >> pip install sympy


def generate_large_prime(bits):
    # Genera un nombre primer gran amb un nombre determinat de bits.
    while True:
        n = random.getrandbits(bits)
        if isprime(n):
            return n

def generate_keypair(bits):
    # Genera un parell de claus RSA (publica i privada).
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Public Exponent (2^16 + 1)
    e = 65537
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def encrypt(plaintext, pub_key):
    # Encripta un missatge utilitzant la clau pública.
    e, n = pub_key
    plaintext = [ord(char) for char in plaintext]
    ciphertext = [pow(char, e, n) for char in plaintext]
    return ciphertext

def decrypt(ciphertext, priv_key):
    # Desencripta un missatge utilitzant la clau privada.
    d, n = priv_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)



if __name__ == "__main__":
    # Key Generation (only 8 bits for demo -> 2048 in practise)
    pub_key, priv_key = generate_keypair(8)
    
    # Encrypt and decrypt a message:
    message = "Hola"
    print("Missatge original:", message)
    
    encrypted_message = encrypt(message, pub_key)
    print("Missatge encriptat:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message, priv_key)
    print("Missatge desencriptat:", decrypted_message)

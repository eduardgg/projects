
# ECC Encryption Project
# This project implements elliptic curve crytography (ECC) using Python and "cryptography" library
# Need to install library: >> pip install cryptography

from ecc import ECC

def main():
    ecc = ECC()
    
    private_pem, public_pem = ecc.generate_keys()
    print("Private Key:\n", private_pem.decode())
    print("Public Key:\n", public_pem.decode())
    
    # Encrypt
    plaintext = "Hello, ellyptic curve!"
    ciphertext, nonce = ecc.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    
    # Decrypt
    decrypted_message = ecc.decrypt(ciphertext, nonce)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()

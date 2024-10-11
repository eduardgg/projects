from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generar una clau RSA
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Serialitzar la clau privada a un format que pugui ser exposat
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Emmagatzemar o transmetre la clau privada (perillós si no es protegeix adequadament)
print(private_pem.decode())  # Exposar la clau privada a la sortida


import random

# Corba el·líptica
class EC_Curve:
    def __init__(self, a_coef, b_coef, prime_mod):
        self.a = a_coef
        self.b = b_coef
        self.p = prime_mod

    def check_point(self, point):
        if point is None:
            return True
        x, y = point
        return (x**3 + self.a * x + self.b - y**2) % self.p == 0

    def add_points(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y1 != y2: return None  # P + (-P) = punt a l'infinit
        
        if P == Q: slope = (3 * x1**2 + self.a) * pow(2 * y1, self.p - 2, self.p)
        else: slope = (y2 - y1) * pow(x2 - x1, self.p - 2, self.p)
        slope %= self.p
        x3 = (slope**2 - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def mult_point(self, k, P):
        result = None
        addend = P

        while k:
            if k & 1: result = self.add_points(result, addend)
            addend = self.add_points(addend, addend)
            k >>= 1

        return result

# Definim paràmetres de la EC
prime_mod = 137
a_coef = 5
b_coef = 7

# Definim corba: y^2 = x^3 + ax + b (mod p)
curve = EC_Curve(a_coef, b_coef, prime_mod)

# Punt generador (sobre la corba) -> Ho comprovem
G_point = (15, 13)
assert curve.check_point(G_point), "El punt generador no pertany a la corba"

# Generació de claus pública i privada
def key_pair_gen():
    private = random.randint(1, prime_mod - 1)
    public = curve.mult_point(private, G_point)
    return private, public

# Xifratge ElGamal
def encrypt_message(curve, pub_key, msg_point, generator):
    random_key = random.randint(1, prime_mod - 1)
    C1 = curve.mult_point(random_key, generator)
    C2 = curve.add_points(msg_point, curve.mult_point(random_key, pub_key))
    return C1, C2

def decrypt_message(curve, priv_key, C1, C2):
    shared_secret = curve.mult_point(priv_key, C1)
    S_inv = (shared_secret[0], -shared_secret[1] % prime_mod)
    original_msg = curve.add_points(C2, S_inv)
    return original_msg

# Missatge (sobre la corba) -> Ho comprovem
msg = (60, 11)
assert curve.check_point(msg), "El missatge no pertany a la corba"

# Genera el parell de claus
private_key, public_key = key_pair_gen()
print("Clau privada", private_key)
print("Clau pública", public_key)

# Xifrar el missatge
cipher_C1, cipher_C2 = encrypt_message(curve, public_key, msg, G_point)
print("Missatge xifrat: C1 = ", cipher_C1, " C2 = ", cipher_C2)

# Desxifrar el missatge
decrypted_msg = decrypt_message(curve, private_key, cipher_C1, cipher_C2)
print("Missatge desxifrat: ", decrypted_msg)

import random

# Definim la corba el·líptica
class EC_Curve:
    def __init__(self, a_coef, b_coef, prime_mod):
        self.a = a_coef
        self.b = b_coef
        self.p = prime_mod  # Mòdul primer

    # Comprova si un punt es troba sobre la corba
    def check_point(self, point):
        if point is None:  # El punt a l'infinit
            return True
        x, y = point
        return (y**2) % self.p == (x**3 + self.a * x + self.b) % self.p

    # Suma de dos punts sobre la corba
    def add_points(self, P, Q):
        if P is None:
            return Q
        if Q is None:
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 != y2:
            return None  # P + (-P) = punt a l'infinit

        if P == Q:
            # Duplicació de punt
            slope = (3 * x1**2 + self.a) * pow(2 * y1, self.p - 2, self.p)
        else:
            # Suma de punts diferents
            slope = (y2 - y1) * pow(x2 - x1, self.p - 2, self.p)

        slope = slope % self.p
        x3 = (slope**2 - x1 - x2) % self.p
        y3 = (slope * (x1 - x3) - y1) % self.p

        return (x3, y3)

    # Multiplicació escalar (k * P)
    def mult_point(self, k, P):
        result = None  # Punt a l'infinit
        addend = P

        while k:
            if k & 1:
                result = self.add_points(result, addend)
            addend = self.add_points(addend, addend)
            k >>= 1

        return result

    # Troba un punt que pertanyi a la corba per a un valor de x donat
    def find_point_for_x(self, x):
        # Calcula y^2 = x^3 + ax + b mod p
        rhs = (x**3 + self.a * x + self.b) % self.p
        # Cerca un valor de y tal que y^2 = rhs mod p
        for y in range(self.p):
            if (y**2) % self.p == rhs:
                return (x, y)  # Retorna el punt (x, y)
        return None  # No s'ha trobat cap punt per aquest x


# Paràmetres de la corba el·líptica
prime_mod = 137  # Un primer més gran
a_coef = 5
b_coef = 7

# Corba: y^2 = x^3 + ax + b mod prime_mod
curve = EC_Curve(a_coef, b_coef, prime_mod)

# Punt generador (més aleatori) a sobre la corba
G_point = (15, 13)

# Verifica que el punt generador està sobre la corba
assert curve.check_point(G_point), "El punt generador no pertany a la corba"

# Generació de claus
def key_pair_gen():
    private = random.randint(1, prime_mod - 1)  # Clau privada
    public = curve.mult_point(private, G_point)  # Clau pública
    return private, public

# Algorisme de xifrat ElGamal
def encrypt_message(curve, pub_key, msg_point, generator):
    random_key = random.randint(1, prime_mod - 1)
    C1 = curve.mult_point(random_key, generator)  # C1 = k * G
    C2 = curve.add_points(msg_point, curve.mult_point(random_key, pub_key))  # C2 = M + k * P_pub
    return C1, C2

# Algorisme de desxifrat ElGamal
def decrypt_message(curve, priv_key, C1, C2):
    shared_secret = curve.mult_point(priv_key, C1)  # S = priv_key * C1
    S_inv = (shared_secret[0], -shared_secret[1] % prime_mod)  # Invers del punt S
    original_msg = curve.add_points(C2, S_inv)  # M = C2 - S
    return original_msg

# Troba un punt vàlid per al missatge
x_value = 60  # Escollim un valor de x aleatori
msg_point = curve.find_point_for_x(x_value)

if msg_point is None:
    print(f"No s'ha trobat cap punt per x = {x_value}.")
else:
    print(f"Missatge (punt) trobat: {msg_point}")

    # Genera el parell de claus
    private_key, public_key = key_pair_gen()

    print(f"Clau privada: {private_key}")
    print(f"Clau pública: {public_key}")

    # Xifrar el missatge
    cipher_C1, cipher_C2 = encrypt_message(curve, public_key, msg_point, G_point)
    print(f"Missatge xifrat: C1 = {cipher_C1}, C2 = {cipher_C2}")

    # Desxifrar el missatge
    decrypted_msg = decrypt_message(curve, private_key, cipher_C1, cipher_C2)
    print(f"Missatge desxifrat: {decrypted_msg}")

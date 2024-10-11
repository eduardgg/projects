# Manipulació de bits en Python

# Definim el valor de n
n = 43
print("=== Representació binària ===")
print(f"El nombre n val {n}")
print(f"La representació binària amb prefix és {bin(n)}")  # amb prefix '0b'
print(f"La representació binària és {format(n, 'b')}")  # sense prefix
print(f"El nombre de bits totals és {n.bit_length()}")  # nombre de bits per representar el nombre
print(f"El nombre de bits '1' (bits encesos) és {n.bit_count()}")  # bits encesos

# Operacions de desplaçament
print(f"El desplaçament a l'esquerra (n << 1) és {format(n << 1, 'b')} (o sigui, {n << 1})")  # x * 2^k
print(f"El desplaçament a la dreta (n >> 1) és {format(n >> 1, 'b')} (o sigui, {n >> 1})")  # x // 2^k
print(f"x << k correspon a x*2^k: 3 << 4 = {3 << 4}")  # 3 * 2^4 = 48
print(f"x >> k correspon a x//2^k: 31 >> 3 = {31 >> 3}")  # 31 // 2^3 = 3

# Operació complement
print(f"El complement a dos (bitwise NOT) de n = {n} és ~n = {~n}")

print("\n=== Operacions amb bits ===")
a = 60  # 0011 1100
b = 13  # 0000 1101
print(f"a = {a} ({bin(a)}), b = {b} ({bin(b)})")
print(f"a & b (AND bit a bit): {a & b} ({bin(a & b)})")  # resultat 0000 1100
print(f"a | b (OR bit a bit): {a | b} ({bin(a | b)})")  # resultat 0011 1101
print(f"a ^ b (XOR bit a bit): {a ^ b} ({bin(a ^ b)})")  # resultat 0011 0001

print("\n=== Manipulació de bits ===")
# Potències de dos utilitzant desplaçament
print("La potència 2^i es pot calcular com 1 << i")
for i in range(5):
    print(f"1 << {i} = {1 << i}")  # Potències de dos: 1, 2, 4, 8, 16...

# Com saber si un nombre és parell o senar
x = 43
print(f"x = {x} ({bin(x)})")
print(f"x és parell si x & 1 = 0, o senar si x & 1 = 1: {x & 1} -> {'senar' if x & 1 else 'parell'}")

# Saber si un nombre és divisible per 2^k
k = 3
print(f"x = {x} és divisible per 2^{k} si x & (2^{k} - 1) = 0: {x & (2**k - 1)}")

# Manipulació directa de bits específics
k = 2  # Modificarem el k-èssim bit
print(f"x = {x}, k = {k}")
print(f"x & (1 << {k}) comprova el {k}-èssim bit: {x & (1 << k)}")
print(f"x | (1 << {k}) posa el {k}-èssim bit a 1: {x | (1 << k)}")
print(f"x & ~ (1 << {k}) posa el {k}-èssim bit a 0: {x & ~(1 << k)}")
print(f"x ^ (1 << {k}) inverteix el {k}-èssim bit: {x ^ (1 << k)}")

# Més manipulació de bits
print(f"x & (x-1) posa el bit '1' menys significatiu a 0: {x & (x-1)}")
if (x & (x-1)) == 0:
    print(f"x = {x} és una potència de 2 (només té un 1)")
else:
    print(f"x = {x} no és una potència de 2")

print(f"x & -x deixa només el bit '1' menys significatiu: {x & -x}")
print("Aquest nombre és la major potència 2^i que divideix x")

print("\n=== Operacions de conjunts (emulació amb bits) ===")
# Emulació de conjunts amb bits
print("Els bits poden emular conjunts. Exemples:")
set1 = 0b1010  # Conjunt 1: {1, 3}
set2 = 0b1100  # Conjunt 2: {2, 3}
print(f"Set1 = {bin(set1)} (elements {{1, 3}}), Set2 = {bin(set2)} (elements {{2, 3}})")

# Operacions amb conjunts
print(f"Intersecció (AND): Set1 & Set2 = {bin(set1 & set2)} (elements comuns)")
print(f"Unió (OR): Set1 | Set2 = {bin(set1 | set2)} (tots els elements)")
print(f"Diferència simètrica (XOR): Set1 ^ Set2 = {bin(set1 ^ set2)} (elements diferents)")
print(f"Complement de Set1 (NOT): ~Set1 = {bin(~set1 & 0b1111)} (inversió dels elements fins a 4 bits)")

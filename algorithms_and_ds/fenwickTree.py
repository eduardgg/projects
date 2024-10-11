
# Fenwick tree
# És una implementació eficient per calcular sumes de segments
# similar a segment tree, però millor (i específic) per sumes

def fw_create(t):
    # Es modifica t
    for i in range(len(t)):
        c = t[i]
        i = i | i+1
        if i < len(t):
            t[i] += c
    return t

def fw_query(t, i):
    s = 0
    while i:
        s += t[i-1]
        i = i & i-1
    return s

def fw_update(t, i, c):
    while i < len(t):
        t[i] += c
        i = i | i+1

# Exemple d'ús:
t = [3,7,2,3,6,4,4,6,9]
fw = fw_create(t)
print(fw)
print(fw_query(t, 4))
print(fw_query(t, 7))
fw_update(t, 2, 9)
print(t)
print(fw_query(t, 2))
print(fw_query(t, 3))




# EXTRA:
# Inversió d'un Fenwick Tree
def fw_inverse(t):
    w = [[] for _ in range(len(t))]
    for i in range(len(w)):
        j = i | i+1
        if j < len(w):
            w[j].append(i)
    # Es modifica t
    for j in range(len(t)-1, -1, -1):
        for i in w[j]:
            t[j] -= t[i]
    return t
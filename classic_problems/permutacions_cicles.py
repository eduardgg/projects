import random

# Les permutacions són vectors V amb valors entre 0 i n-1
# Les escrivim entre 1 i n al final de tot, únicament per repotar resultats

def random_perm(n):
    v = n*[0]
    for i in range(n):
        v[i] = i
    for i in range(n):
        j = random.randint(i,n-1)
        v[i],v[j] = v[j],v[i]
    return [x for x in v]

def cycles_perm(v):
    m = len(v)
    vist = [0]*m
    longituds = []
    for i in range(m):
        if vist[i] == 0:
            inicial = i
            vist[inicial] = 1
            següent = v[inicial]
            vist[següent] = 1
            longitud = 1
            while (següent != inicial):
                següent = v[següent]
                vist[següent] = 1
                longitud += 1
            longituds.append(longitud)
    return longituds

R = random_perm(100)
print([x+1 for x in R])
print("Hi ha un total de " + str(len(cycles_perm(R))) + " cicles.")
print("Les seves longituds són " + str(cycles_perm(R)) + '.')

# Anem a aproximar la probabilitat que tots els cicles d'una permutació
# de tamany 100 tinguin una longitud menor a 50 i que, per tant, els 
# presoners del problema tenen aquesta probabilitat de sobreviure.
comptador = 0
trials = 10000
for i in range(trials):
    R = random_perm(100)
    if max(cycles_perm(R)) <= 50:
        comptador += 1
print(comptador/trials)

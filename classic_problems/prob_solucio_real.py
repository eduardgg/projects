
import random as rd

# Càlcul de la probabilitat de solució real:
# Equació: axx + bx + c = 0
# Paràmetres: a, b, c ~ U[0, 1]`

cont = 0
reps = int(input())
for i in range(reps):
    a = rd.random()
    b = rd.random()
    c = rd.random()
    if b**2 - 4*a*c > 0:
        cont += 1

# Com més repeticions, més fiabilitat del resultat
print (cont/reps)

import random

def randPerm(n):
    elements = list(range(1, n+1))
    random.shuffle(elements)
    return elements

def cyclesPerm(p):
    n = len(p)
    cycles = {}
    fet = [False]*n
    for i in range(n):
        if fet[i]:
            continue
        cl = 0
        while not fet[i]:
            cl += 1
            fet[i] = True
            i = p[i]-1
        cycles[cl] = cycles.get(cl, 0) + 1
    return cycles



n = 100
count = 0
t = 100000
# d = Nombre de vegades en què p és un desarranjament.
# (fent servir t = 100000 test cases)
for i in range(t):
    p = randPerm(n)
    c = cyclesPerm(p)
    if c.get(1, 0):
        count += 1
ans = 100*(1 - count/t)
print(ans, "%")
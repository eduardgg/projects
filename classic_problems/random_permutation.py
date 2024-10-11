
import random

def randPerm1(n):
    elements = list(range(1, n+1))
    random.shuffle(elements)
    return elements

def randPerm2(n):
    els = list(range(1, n+1))
    for i in range(n):
        j = random.randint(i, n-1)
        els[i], els[j] = els[j], els[i]
    return els


rp1 = randPerm1(6)
print(*rp1)

rp2 = randPerm2(7)
print(*rp2)
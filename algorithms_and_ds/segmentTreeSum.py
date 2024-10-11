
# ST = Segment Tree
# Aquesta estructura de dades serveix per calcular propietats d'interval eficientment.
# Això inclou suma, mínims, màxims i altres. Però per sumes no és tan eficient com l'ABI.

class ST():
    
    def __init__(self, v):
        self.v = v
        self.len = 2**(len(v)-1).bit_length()
        self.tree = [0]*self.len + v + [0]*(self.len - len(v))
        k = self.len
        while k > 1:
            for i in range(k, 2*k):
                self.tree[i//2] += self.tree[i]
            k //= 2
    
    def add(self, k, x):
        k += self.len
        self.tree[k] += x        
        while k > 1:
            k //= 2
            self.tree[k] = self.tree[2*k] + self.tree[2*k+1]

    def sum(self, a, b):
        a += self.len - 1
        b += self.len - 1
        s = 0
        while a <= b:
            if a%2 == 1:
                s += self.tree[a]
                a += 1
            if b%2 == 0:
                s += self.tree[b]
                b -= 1
            a //= 2
            b //= 2
        return s
    
        

v = [5,8,6,3,2,7,2,6,5]
segmentTree = ST(v)
print(v)
print(segmentTree.len)
print(segmentTree.tree)
print(segmentTree.sum(4,6))
segmentTree.add(3, 2)
print(segmentTree.tree)
print(segmentTree.sum(4,6))

# ST = Segment Tree
# Aquesta estructura de dades serveix per calcular propietats d'interval eficientment.
# Això inclou suma, mínims, màxims i altres. Però per sumes no és tan eficient com l'ABI.

class ST():
    
    def __init__(self, v):
        self.v = v
        self.len = 2**(len(v)-1).bit_length()
        l = self.len
        inf = float('-inf')
        self.tree = [inf]*l + v + [inf]*(l-len(v))
        
        while l > 1:
            for i in range(l, 2*l):
                self.tree[i//2] = max(self.tree[i//2], self.tree[i])
            l //= 2
    
    def change(self, k, x):
        k += self.len
        self.tree[k] = x
        while k > 1:
            k //= 2
            self.tree[k] = max(self.tree[2*k], self.tree[2*k+1])

    def maxim(self, a, b):
        a += self.len - 1
        b += self.len - 1
        s = float('-inf')
        while a <= b:
            if a%2 == 1:
                s = max(s, self.tree[a])
                a += 1
            if b%2 == 0:
                s = max(s, self.tree[b])
                b -= 1
            a //= 2
            b //= 2
        return s
    
        

v = [5,8,6,3,2,7,2,6,5]
segmentTree = ST(v)
print(v)
print(segmentTree.len)
print(segmentTree.tree)
print(segmentTree.maxim(4,6))

segmentTree.change(3, 4)
# (a, b) -> a posició (començant en 0), b element nou

print(segmentTree.tree)
print(segmentTree.maxim(4,6))
print(segmentTree.maxim(2,3))
# (a, b) -> a, b posicions (incloses, i començant en 1)

segmentTree.change(4, 5)
segmentTree.change(6, 9)
print(segmentTree.maxim(1, len(segmentTree.v)))
print(len(segmentTree.v))
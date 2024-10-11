
# ABI = Arbre Binari Indexat
# Aquesta estructura de dades serveix per calcular sumes de segments eficientment.
# No serveix per calcular mínims ni màxims de segments, per això cal un segment tree.

class ABI():
    
    def __init__(self, v):
        self.v = v
        self.length = len(v)
        self.tree = [0]*self.length
        for i in range(self.length): 
            self.add(i, v[i])
    
    def add(self, k, x):
        while k < self.length:
            self.tree[k] += x
            k += (k+1)&-(k+1)

    def sum(self, k):
        s = 0
        while k >= 1:
            s += self.tree[k]
            k -= (k+1)&-(k+1)
        return s

    def segment(self, k, q):
        return self.sum(q) - self.sum(k-1)

        
        

v = [1,3,4,8,6,1,4,2,3,5,2,8,7]
abi = ABI(v)
print(abi.tree) # [1, 4, 4, 16, 6, 7, 4, 29, 3, 8, 2, 18, 7]
print(abi.segment(4,10)) # 6 + 1 + 4 + 2 + 3 + 5 = 23
abi.add(2, 3)
print(abi.tree) # [1, 4, 7, 19, 6, 7, 4, 32, 3, 8, 2, 18, 7]
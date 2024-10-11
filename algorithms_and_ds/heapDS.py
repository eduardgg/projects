class Heap:
    
    def __init__(self, v):
        self.vector = v
    
    def longitud(self):
        return len(self.vector)
    
    def insert(self, a):
        self.vector += [a]
        pos = len(self.vector) - 1
        while pos > 0 and self.vector[pos] < self.vector[(pos-1)//2]:
            pare = (pos-1)//2
            self.vector[pos], self.vector[pare] = self.vector[pare], self.vector[pos]
            pos = pare

    def checkHeap(self):
        for i in range(1, self.longitud()):
            if self.vector[i] < self.vector[(i-1)//2]:
                return False
        return True

    def heapify(self):
        toHeapify = self.vector
        self.vector = []
        for e in toHeapify:
            self.insert(e)
        return
    
    def minim(self):
        return self.vector[0]

    def extractMin(self):
        if self.longitud() == 0:
            return None
        
        minim = self.vector[0]
        self.vector[0] = self.vector.pop()
        pos = 0
        
        while self.longitud() > 2*pos + 2:
            minNode = min(self.vector[pos], self.vector[2*pos+1], self.vector[2*pos+2]) 
            if minNode == self.vector[pos]:
                break
            elif minNode == self.vector[2*pos+1]:
                self.vector[pos], self.vector[2*pos + 1] = self.vector[2*pos + 1], self.vector[pos]
                pos = 2*pos + 1
            else:
                self.vector[pos], self.vector[2*pos + 2] = self.vector[2*pos + 2], self.vector[pos]    
                pos = 2*pos + 2

        if self.longitud() == 2*pos + 2 and self.vector[pos] > self.vector[2*pos+1]:
            self.vector[pos], self.vector[2*pos + 1] = self.vector[2*pos + 1], self.vector[pos]

        return minim


    def printHeap(self):
        # TODO
        return                



h = Heap([5,6,3,9,10,2,-4,0,-2,6,5,6,1])
print(h.vector)
# print(h.longitud())
print(h.checkHeap())
h.heapify()
print(h.vector)
print(h.checkHeap())
"""
for i in range(6):
    print(h.extractMin())
    print(h.vector)
"""
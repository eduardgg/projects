import sys
 
class MinHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
 
    def parent(self, pos):
        return pos // 2
 
    def leftChild(self, pos):
        return 2 * pos
 
    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if pos > self.size // 2 and pos <= self.size:
            return True
        return False
 
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
 
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
 
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
 
    def printHeap(self):
        if self.size % 2 == 1:
            for i in range(1, self.size // 2 + 1):
                print("    PARENT: " + str(self.Heap[i]) +
                ", LEFT CHILD: " + str(self.Heap[2 * i]) +
                ", RIGHT CHILD: " + str(self.Heap[2 * i + 1]))
            return
        for i in range(1, self.size // 2):
            print("    PARENT: " + str(self.Heap[i]) +
            ", LEFT CHILD: " + str(self.Heap[2 * i]) +
            ", RIGHT CHILD: " + str(self.Heap[2 * i + 1]))
        i = self.size // 2
        print("    PARENT: " + str(self.Heap[i]) +
        ", LEFT CHILD: " + str(self.Heap[2 * i]))
        
        """
        # Aquest fragment no era del tot correcte:
        for i in range(1, (self.size//2)+1):
            print("    PARENT: " + str(self.Heap[i]) +
            ", LEFT CHILD: " + str(self.Heap[2 * i]) +
            ", RIGHT CHILD: " + str(self.Heap[2 * i + 1]))
        """
 
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
 
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped
    
    # VIGILAR: Aquest mètode modifica el heap
    # (treu els menors elements)
    def nSmallest(self, n):
        vec = []
        copy = self
        for i in range(n):
            a = copy.remove()
            vec += [a]
        return vec
    
    def printHeapMeu(self):
        v = self.Heap
        n = self.size
        log = 0
        while n > 1:
            n = n // 2
            log += 1
        pos = 1
        for i in range(log+1):
            for j in range(2**i):
                print(str(v[pos+j]), end = " ")
            print()
            pos += 2**i

MH = MinHeap(31)
MH.insert(2)
MH.insert(5)
MH.insert(9)
MH.insert(4)
MH.insert(13)
MH.insert(7)
MH.printHeap()

MH.printHeapMeu()

"""
print(MH.nSmallest(4))
MH.printHeap()
MH.remove()
MH.printHeap()
"""
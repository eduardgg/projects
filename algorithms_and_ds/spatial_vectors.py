import math

class SpatialVector:
    def __init__(self, a):
        self._coords = a
    def __len__(self):
        return len(self._coords)
    def __add__(self,other):
        if len(self) != len(other):
            return "Error"
        s = SpatialVector([0]*len(self))
        for i in range(len(self)):
            s._coords[i] = self._coords[i] + other._coords[i]
        return s
    def scalarProduct(self,a):
        s = SpatialVector([0]*len(self))
        for i in range(len(self)):
            s._coords[i] = a*self._coords[i]
        return s
    def dotProduct(self,other):
        return sum(self._coords[i] * other._coords[i] for i in range(len(self)))
    def magnitude(self):
        return math.sqrt(sum(self._coords[i] * self._coords[i] for i in range(len(self))))
    def direction(self):
        d = SpatialVector([0]*len(self))
        for i in range(len(self)):
            d._coords[i] = self._coords[i]*(1/self.magnitude())
        return d
    def __str__(self):
        return str(self._coords)

a = [1,0,-1,2,0]
b = [0,2,-3,-8,4]
v = SpatialVector(a)
w = SpatialVector(b)
print(v + w)
print(v.scalarProduct(5))
print(v.dotProduct(w))
print(v.magnitude())
print(v.direction())
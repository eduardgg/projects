import random
import numpy
from matplotlib import pyplot as plt 

n = 1000
a = [0]
cont = {}
for i in range(n):
    r = random.randint(0, len(a)-1)
    a = a + [a[r]+1]
    cont[a[r]+1] = cont.get(a[r]+1,0) + 1
print(cont)

m = max(cont.keys())
a = []
for i in range(m):
    a = a + [cont.get(i+1,0)]
print(a)

plt.bar(cont.keys(), cont.values(), width=1, color='g')
plt.title("Histograma") 
plt.show()


"""
a = numpy.histogram(d, bins=10, range=None, normed=None, weights=None, density=None)
d = numpy.random.laplace(loc=15, scale=3, size=500)
print(d)
plt.hist(d)
plt.title("histogram") 
plt.show()
"""
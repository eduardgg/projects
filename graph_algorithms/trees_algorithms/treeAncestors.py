
# k - Ancestors:
nodes = [1, 2, 3, 4, 5, 6, 7, 8]
parents = [0, 1, 4, 1, 1, 2, 4, 7]
n = len(nodes)
m = n.bit_length()
print(n, m)
ancestors = [[-1 for _ in range(m+1)] for _ in range(n)]

for x in nodes:
    ancestors[x-1][0] = x
    ancestors[x-1][1] = parents[x-1]

for x in nodes:
    for i in range(2, m+1):
        # Cada i fa referència a 2^i pisos
        ancestors[x-1][i] = ancestors[max(0,ancestors[x-1][i-1]-1)][i-1]

def ancestor(x, k):
    # Aquesta k fa referència a k pisos
    if x < 0 or k < 0:
        return None
    if x == 0:
        return 0
    if k == 0:
        return x
    if k == 1:
        return parents[x-1]
    return ancestor(ancestors[x-1][k.bit_length()], k - (1<<(k.bit_length()-1)))

for i in range(len(ancestors)):
    print(ancestors[i])

print(ancestor(3,1))
print(ancestor(8,1))
print(ancestor(6,1))
print(ancestor(3,2))
print(ancestor(4,2))
print(ancestor(8,2))
print(ancestor(5,2))
print(ancestor(8,3))
print(ancestor(8,4))
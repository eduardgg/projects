
# Estructura union-find (DSU)
# Implementació meva, molt senzilla.

n = 10
rank = [1]*(n+1)
leader = [i for i in range(n+1)]

def find(u):
    if leader[u] == u:
        return u
    leader[u] = find(leader[u])
    return leader[u]

def union(a, b):
    la = leader[a]
    lb = leader[b]
    if rank[la] > rank[lb]:
        leader[lb] = la
    elif rank[la] < rank[lb]:
        leader[la] = lb
    else:
        leader[lb] = la
        rank[la] += 1
    return
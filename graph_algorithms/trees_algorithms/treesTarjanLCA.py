from collections import defaultdict
# Està malament! Sembla que al 2n cas falla la query (7, 15). Investigar!

def union(u, v):
    rootU = find(u)
    rootV = find(v)
    if rank[u] > rank[v]:
        parent[v] = rootU
    elif rank[u] < rank[v]:
        parent[u] = rootV
    else:
        parent[u] = rootV
        rank[rootU] += 1
        # No hauria d'augmentar el rank de rootV?

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def tarjan(u):
    parent[u] = u
    rank[u] = 1
    ancestor[u] = u
    for v in children[u]:
        tarjan(v)
        union(u, v)
        ancestor[find(v)] = u
    visited[u] = True
    for v in dicQueries[u]:
        if visited[v]:
            print(f"Tarjan's LCA of {u} and {v} is {ancestor[find(v)]}")




children = [[], [2,3], [4,5], [6,7], [], [], [], []]
queries = [(2,4), (2,7), (3,6), (1, 6)]
dicQueries = defaultdict(list)
for (i, j) in queries:
    dicQueries[i].append(j)
    dicQueries[j].append(i)
n = len(children)
visited = [False]*n
rank = [0]*n
parent = [-1]*n
ancestor = [0]*n
tarjan(1)
print()

children = [[], [2,3,4], [5,6], [7], [], [], [8], [9,10,11], [], [], [12,13], [14], [], [], [15], []]
queries = [(2,4), (8,13), (6,11), (7,15), (9,11), (13,14), (12,13), (11,15), (15,14)]
dicQueries = defaultdict(list)
for (i, j) in queries:
    dicQueries[i].append(j)
    dicQueries[j].append(i)
n = len(children)
visited = [False]*n
rank = [0]*n
parent = [-1]*n
ancestor = [0]*n
tarjan(1)
print()
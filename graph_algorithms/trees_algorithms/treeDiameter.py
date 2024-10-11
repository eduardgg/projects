
G = {1:[2,3,4], 2:[1,5,6], 3:[1], 4:[1,7], 5:[2], 6:[2], 7:[4,8,9], 8:[7], 9:[7]}

def calcLens(v, ant):
    if len(G[v]) == 1:
        toLeaf[v-1] = 0
        maxLen[v-1] = 0
        return
    elif len(G[v]) == 2:
        w = sum(G[v]) - ant
        calcLens(w, v)
        toLeaf[v-1] = 1 + toLeaf[w-1]
        maxLen[v-1] = 0
        return
    for w in G[v]:
        if w == ant:
            continue
        calcLens(w, v)
    vec = [toLeaf[w-1] for w in G[v] if w != ant]
    maxs = heapq.nlargest(2, vec)
    toLeaf[v-1] = 1 + maxs[0]
    maxLen[v-1] = 2 + maxs[0] + maxs[1]

import heapq
toLeaf = [-1]*len(G.keys())
maxLen = [-1]*len(G.keys())
calcLens(1, 0)
diameter = max(maxLen)
print(toLeaf)
print(maxLen)
print("Diameter is", diameter)
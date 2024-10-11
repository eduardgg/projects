
G = {1:[2,3,4], 2:[1,5,6], 3:[1], 4:[1,7], 5:[2], 6:[2], 7:[4,8,9], 8:[7], 9:[7]}

def dfs(v, ant):
    if ant == 0:
        dist[v-1] = 0
    else:
        dist[v-1] = 1 + dist[ant-1]
    for w in G[v]:
        if w != ant:
            dfs(w, v)


dist = [-1]*len(G.keys())
dfs(1, 0)
print(dist)
millor = 0
for i in range(len(dist)):
    if dist[i] > dist[millor]:
        millor = i

dist = [-1]*len(G.keys())
dfs(millor + 1, 0)
print(dist)
print("Diameter is", max(dist))
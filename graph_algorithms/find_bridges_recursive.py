
def find_bridges(graph):
    
    def dfs(v, parent, time):
        nonlocal id_counter
        ids[v] = low[v] = id_counter
        id_counter += 1

        for to in graph[v]:
            if to == parent:
                continue
            if ids[to] == -1:  # If to is not visited
                dfs(to, v, time + 1)
                low[v] = min(low[v], low[to])
                if ids[v] < low[to]:
                    bridges.append((v, to))
            else:
                low[v] = min(low[v], ids[to])
    
    n = len(graph)
    ids = [-1] * n
    low = [0] * n
    bridges = []
    id_counter = 0

    for i in range(n):
        if ids[i] == -1:
            dfs(i, -1, 0)

    return bridges

# Exemples d'ús:
# Representació del graf amb llistes d'adjacència
graph = [
    [1, 2],        # 0
    [0, 2],        # 1
    [0, 1, 3],     # 2
    [2, 4],        # 3
    [3]            # 4
]

print(find_bridges(graph))
# Sortida: [(3, 4), (2, 3)]


def find_bridges_iterative(graph):

    n = len(graph)
    ids = [-1] * n
    low = [0] * n
    bridges = []
    id_counter = 0
    stack = []
    parent = [-1] * n

    for i in range(n):
        if ids[i] == -1:
            stack.append((i, iter(graph[i])))
            ids[i] = low[i] = id_counter
            id_counter += 1

            while stack:
                v, children = stack[-1]
                for to in children:
                    if ids[to] == -1:
                        stack.append((to, iter(graph[to])))
                        parent[to] = v
                        ids[to] = low[to] = id_counter
                        id_counter += 1
                        break
                    elif to != parent[v]:
                        low[v] = min(low[v], ids[to])
                else:
                    stack.pop()
                    if parent[v] != -1:
                        low[parent[v]] = min(low[parent[v]], low[v])
                        if ids[parent[v]] < low[v]:
                            bridges.append((parent[v], v))

    return bridges

# Exemples d'ús:
graph = [
    [1, 2],        # 0
    [0, 2],        # 1
    [0, 1, 3],     # 2
    [2, 4],        # 3
    [3]            # 4
]

print(find_bridges_iterative(graph))  # Sortida: [(2, 3), (3, 4)]

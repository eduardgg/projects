
graph = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0]
]

nodes = len(graph)
path = [0] + [-1]*(nodes-1)
visited = {0}

def f(v):
    m = len(visited)
    if m == nodes and graph[path[-1]][0] == 1:
        print(path)
        return
    for i in range(nodes):
        if graph[v][i] == 1 and (i not in visited):
            path[m] = i
            visited.add(i)
            f(i)
            visited.remove(i)

f(0)
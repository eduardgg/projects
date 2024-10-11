from collections import defaultdict

def kosaraju(graph):

    visited = set()
    ordre = []
    for node in graph:
        if node not in visited:
            stack = [node]
            while(stack):
                v = stack[-1]
                if v in visited:
                    ordre.append(stack.pop())
                    continue
                visited.add(v)
                for neighbor in graph.get(v, []):
                    if neighbor not in visited:
                        stack.append(neighbor)

    reversed_graph = defaultdict(list)
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)
    
    visited = set()
    components = []
    while ordre:
        node = ordre.pop()
        if node not in visited:
            component = []
            stack = [node]
            while(stack):
                v = stack.pop()
                component.append(v)
                visited.add(v)
                for neighbor in reversed_graph[v]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            components.append(component)

    return components






graf_unic_cfc = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [6],
    6: [7],
    7: [8],
    8: [9],
    9: [10],
    10: []
}

graf_scc = {
    1: [2],
    2: [3],
    3: [4],
    4: [1],
    5: [1, 6],
    6: [7],
    7: [5]
}

print(kosaraju(graf_unic_cfc))
print(kosaraju(graf_scc))
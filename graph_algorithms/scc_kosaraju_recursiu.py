from collections import defaultdict

def kosaraju(graph):

    def dfs_first_pass(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_first_pass(neighbor)
        stack.append(node)

    def dfs_second_pass(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph[node]:
            if neighbor not in visited:
                dfs_second_pass(neighbor, component)

    visited = set()
    stack = []
    reversed_graph = defaultdict(list)

    # Primera passada per omplir la pila en l'ordre correcte
    for node in graph:
        if node not in visited:
            dfs_first_pass(node)

    # print("Ordre: ", stack)

    # Inverteix les arestes del graf
    for node in graph:
        for neighbor in graph[node]:
            reversed_graph[neighbor].append(node)

    visited = set()
    components = []

    # Segona passada per identificar les CFC
    while stack:
        node = stack.pop()
        if node not in visited:
            component = []
            dfs_second_pass(node, component)
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


cfc_resultat = kosaraju(graf_unic_cfc)
print(cfc_resultat)

cfc_resultat = kosaraju(graf_scc)
print(cfc_resultat)
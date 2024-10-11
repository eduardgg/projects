
graf = {
    0: [1, 3],
    1: [2, 3],
    2: [3, 4],
    3: [4],
    4: [5],
    5: []
}

def topologicalSort(graf):

    def dfs(node):
        visitats.add(node)
        for vei in graf[node]:
            if vei not in visitats:
                dfs(vei)
        ordenament.append(node)
        return

    visitats = set()
    ordenament = []
    for node in graf.keys():
        if node not in visitats:
            dfs(node)
    return ordenament[::-1]

print(topologicalSort(graf))


def tarjan(graph):
    index = [0]  # Variable per a mantenir el comptador dels índexos DFS
    stack = []   # Pila per a mantenir els vèrtexs visitats temporalment
    result = []  # Llista per a guardar les CFC trobades
    graus = {}   # Diccionari per a guardar el grau de cada vèrtex

    def strongconnect(v):
        grau = index[0]
        index[0] += 1
        graus[v] = grau
        stack.append(v)
        onStack[grau] = True

        for w in graph[v]:
            if w not in graus:
                strongconnect(w)
                lowlink[grau] = min(lowlink[graus[v]], lowlink[graus[w]])
            elif onStack[graus[w]]:
                lowlink[grau] = min(lowlink[graus[v]], graus[w])

        if lowlink[graus[v]] == graus[v]:
            scc = []
            while True:
                w = stack.pop()
                onStack[graus[w]] = False
                scc.append(w)
                if w == v:
                    break
            result.append(scc)

    for v in range(len(graph)):
        if v not in graus:
            strongconnect(v)

    return result


# L'entrada és un graph g, vector de vectors
g = [[]]
n = len(g)
lowlink = [i for i in range(n)]
onStack = [False]*n
print(tarjan(g))
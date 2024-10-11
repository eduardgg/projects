

def tarjan(graph):

    temps = [0]
    index = [-1]*len(graph.keys())
    lowLink = [-1]*len(graph.keys())
    onStack = [False]*len(graph.keys())
    stack = []
    scc = []

    def strongCon(v):
        index[v-1] = temps[0]
        lowLink[v-1] = temps[0]
        temps[0] += 1
        stack.append(v)
        onStack[v-1] = True

        for w in graph.get(v, []):
            if index[w-1] == -1:
                strongCon(w)
                lowLink[v-1] = min(lowLink[v-1], lowLink[w-1])
            elif onStack[w-1]:
                lowLink[v-1] = min(lowLink[v-1], index[w-1])
        
        if lowLink[v-1] == index[v-1]:
            nouSCC = []
            while True:
                w = stack.pop()
                onStack[w-1] = False  
                nouSCC.append(w)
                if w == v:
                    break
            scc.append(nouSCC)

    for v in graph.keys():
        if index[v-1] == -1:
            strongCon(v)
    
    return scc



graf_linia = {
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

graf_cicle = {
    1: [2],
    2: [3],
    3: [4],
    4: [5],
    5: [6],
    6: [7],
    7: [8],
    8: [9],
    9: [10],
    10: [1]
}

grafSCC1 = {
    1: [2],
    2: [3],
    3: [4],
    4: [1],
    5: [1, 6],
    6: [7],
    7: [5]
}

grafSCC2 = {
    1: [2],
    2: [3],
    3: [1],
    4: [2, 3, 5],
    5: [4, 6],
    6: [3, 7],
    7: [6],
    8: [5, 7, 8]
}


print(tarjan(graf_linia))
print(tarjan(graf_cicle))
print(tarjan(grafSCC1))
print(tarjan(grafSCC2))

from heapq import heappop, heappush

def pruferCode(tree):
    n = len(tree)
    deg = [0]*n
    for v in range(n):
        for w in tree[v]:
            deg[v] += 1
            deg[w] += 1
    fulles = []
    for v in range(n):
        deg[v] //= 2
        if deg[v] == 1:
            heappush(fulles, v)
    # print(deg)
    # print(fulles)

    pc = []
    vist = [False]*n
    while len(pc) < n-3:
        v = heappop(fulles)
        vist[v] = True
        for w in tree[v]:
            if not vist[w]:
                pc.append(w)
                deg[w] -= 1
                if deg[w] == 1:
                    heappush(fulles, w)
    return pc


def treeFromPrufer(prufer):
    l = len(prufer)
    tree = [[] for _ in range(l+3)]
    deg = [0]*(l+3)
    for v in range(l):
        deg[prufer[v]] += 1
    fulles = []
    for v in range(1, l+3):
        if deg[v] == 0:
            heappush(fulles, v)
    
    vist = [False]*(l+3)
    for w in prufer:
        v = heappop(fulles)
        vist[v] = True
        tree[v].append(w)
        tree[w].append(v)
        deg[v] -= 1
        deg[w] -= 1
        if deg[w] == 0:
            heappush(fulles, w)

    tree[fulles[0]].append(fulles[1])
    tree[fulles[1]].append(fulles[0])
    return tree




tree = [[], [4], [3, 4], [2], [1, 2, 5, 6], [4], [4, 7], [6, 8, 9], [7], [7]]
print(pruferCode(tree))

prufer = [4, 2, 4, 4, 6, 7, 7]
print(treeFromPrufer(prufer))
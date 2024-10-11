
def dfs(node, ant):
    for e in tree[node-1]:
        if e != ant:
            pares[e-1] = node
            rec.append(e)
            dfs(e, node)

def size(i, ant):
    sizes[i-1] = 1
    if ant != 0:
        nivell[i-1] = 1 + nivell[ant-1]
    for j in tree[i-1]:
        if j != ant:
            sizes[i-1] += size(j, i)
    return sizes[i-1]

def lca(u, v):
    # Not very efficient (O(n) per query)
    if nivell[u-1] > nivell[v-1]:
        u, v = v, u
    while nivell[u-1] < nivell[v-1]:
        v = pares[v-1]
    while u != v:
        u = pares[u-1]
        v = pares[v-1]
    return u

def distance(u, v):
    w = lca(u, v)
    return nivell[u-1] + nivell[v-1] - 2*nivell[w-1]

def lca2(u, v):
    # TODO:
    # Mètode d'Euler per trobar el LCA de dos nodes.
    # Falta acabar i optimitzar. La idea és agafar l'interval entre u i v
    # del vector depth que obtenim i buscar la posició del mínim 'i'.
    # Llavors, lca2(u, v) serà nouRec[i].
    def dfsEsp(node, ant, pis):
        nouRec.append(node)
        depth.append(pis)
        for e in tree[node-1]:
            if e != ant:
                pares[e-1] = node
                dfsEsp(e, node, pis+1)
                nouRec.append(node)
                depth.append(pis)
    
    nouRec = []
    depth = []
    dfsEsp(1, 0, 1)
    print(nouRec)
    print(depth)
    print(pares)




# ----------------------------------------------

tree = [[2,3,4,5], [1,6], [1], [1,7,8,9], [1], [2], [4], [4], [4]]
n = len(tree)

# Vector recorregut
rec = [1]
pares = [-1]*n
# De pas, calculem el vector de pares, usant 1 com l'original
dfs(1, 0)

# Tamanys dels subarbres
sizes = [-1]*n
nivell = [0] + [-1]*(n-1)
# De pas, calculem el nivell (pis) de cada node, respecte l'original
size(1, 0)

# Tamanys segons l'ordre del recorregut
sizesRec = [sizes[j-1] for j in rec]

print(rec)
print(sizes)
print(sizesRec)
print(nivell)

# Least common ancestor(LCA)
print(lca(6, 4))
print(lca(7, 9))

# Distància entre dos nodes:
print("Distance from 6 to 4 is", distance(6, 4))
print("Distance from 7 to 9 is", distance(7, 9))

# ----------------------------------------------

tree = [[2,3,4], [1,5,6], [1], [1,7], [2], [2,8], [4], [6]]
n = len(tree)

rec = [1]
pares = [-1]*n
dfs(1, 0)
sizes = [-1]*n
nivell = [0] + [-1]*(n-1)
size(1, 0)
sizesRec = [sizes[j-1] for j in rec]

print()
print(rec)
print(sizes)
print(sizesRec)
print(nivell)
print(lca(5, 8))
print(lca(6, 7))
print("Distance from 5 to 4 is", distance(5, 4))
print("Distance from 5 to 8 is", distance(5, 8))
print("Distance from 8 to 7 is", distance(8, 7))
lca2(3, 4)

# ----------------------------------------------
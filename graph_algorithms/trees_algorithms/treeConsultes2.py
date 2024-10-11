
# Find least common ancestor (LCA) of two nodes in a tree
# (efficient solution, using a "Union-Find" (DSU) data structure)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

def find_lca(root, nodes):
    parent = {root.val: None}
    ancestor = {root.val: root.val}
    visited = set()

    def find(node):
        ancestor[node.val] = node.val
        for child in node.children:
            if child.val not in visited:
                parent[child.val] = node.val
                find(child)
                union(node.val, child.val)
        visited.add(node.val)

    def union(u, v):
        ancestor[find_set(u)] = find_set(v)

    def find_set(u):
        if ancestor[u] != u:
            ancestor[u] = find_set(ancestor[u])
        return ancestor[u]

    # Troba el LCA per cada parell de nodes
    def find_lca_pair(u, v):
        set_u = set()
        set_v = set()

        while u is not None or v is not None:
            if u is not None:
                if find_set(u) in set_v:
                    return u
                set_u.add(u)
                u = parent[u]

            if v is not None:
                if find_set(v) in set_u:
                    return v
                set_v.add(v)
                v = parent[v]

    # Executa l'algorisme a l'arrel de l'arbre
    find(root)

    # Troba el LCA per cada parell de nodes
    results = []
    for u, v in nodes:
        lca = find_lca_pair(u, v)
        results.append((u, v, lca))

    return results

# Exemple d'ús:
# Crea un arbre de mostra
root = TreeNode(1)
root.children = [TreeNode(2), TreeNode(3)]
root.children[0].children = [TreeNode(4), TreeNode(5)]
root.children[1].children = [TreeNode(6), TreeNode(7)]

# Troba els LCA per cada parell de nodes
nodes_to_find = [(4, 5), (6, 7), (2, 4)]
result = find_lca(root, nodes_to_find)

# Mostra els resultats
for u, v, lca in result:
    print(f"LCA entre {u} i {v}: {lca}")
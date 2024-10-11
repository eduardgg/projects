
from collections import defaultdict

class Graph:

    def __init__(self, n):
        self.V = n
        self.graph = defaultdict(list)
        self.indegree = [0] * n
        self.outdegree = [0] * n

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.outdegree[u] += 1
        self.indegree[v] += 1

    def has_eulerian_path(self):
        start_nodes = 0
        end_nodes = 0

        for i in range(self.V):
            out_d = self.outdegree[i]
            in_d = self.indegree[i]

            if out_d - in_d == 1:
                start_nodes += 1
            elif in_d - out_d == 1:
                end_nodes += 1
            elif in_d != out_d:
                return False

        # Comprovem les condicions per un camí eulerià:
        return (start_nodes == 1 and end_nodes == 1) or (start_nodes == 0 and end_nodes == 0)

    def dfs(self, u, path):
        # Recorrem les arestes del vèrtex u:
        for v in self.graph[u]:
            if (u, v) in self.visited_edges:
                continue
            self.visited_edges.add((u, v))
            self.dfs(v, path)
        path.append(u)

    def eulerian_path(self):
        if not self.has_eulerian_path():
            return None

        # Trobem el vèrtex d'inici:
        start = 0
        for i in range(self.V):
            if self.outdegree[i] - self.indegree[i] == 1:
                start = i
                break

        self.visited_edges = set()
        path = []
        self.dfs(start, path)

        return path[::-1]

# Exemple d'ús
n = 5  # Nombre de vèrtexos
g = Graph(n)

# Afegir arcs (exemple)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

path = g.eulerian_path()
if path:
    print("Camí eulerià:", path)
else:
    print("No hi ha camí eulerià.")

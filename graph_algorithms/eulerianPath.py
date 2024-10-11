
from collections import defaultdict

class Graph:
    
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):
        visited = set()
        
        # Trobem un vèrtex amb arestes:
        for node in self.graph:
            if len(self.graph[node]) > 0:
                start_node = node
                break

        # DFS a partir del node inicial:
        self.dfs(start_node, visited)

        # Comprovem si tots els nodes amb arestes han estat visitats
        for node in self.graph:
            if len(self.graph[node]) > 0 and node not in visited:
                return False
        return True

    def dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def find_eulerian_path(self):
        if not self.is_connected():
            return "El graf no és connex."

        odd_degree_nodes = [node for node in self.graph if len(self.graph[node]) % 2 == 1]

        if len(odd_degree_nodes) > 2:
            return "No hi ha camí eulerià."

        start_node = odd_degree_nodes[0] if odd_degree_nodes else next(iter(self.graph))
        path = []

        self.find_path_util(start_node, path)

        return path

    def find_path_util(self, u, path):
        for v in self.graph[u]:
            if v is not None:
                # Eliminar aresta
                self.graph[u].remove(v)
                self.graph[v].remove(u)
                self.find_path_util(v, path)
        path.append(u)

# Exemple d'ús
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)
g.add_edge(4, 1)

result = g.find_eulerian_path()
print("El camí eulerià és:", result)


class GrafDirigit:
    
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graf = [[] for _ in range(num_nodes)]
        self.temps = 0
        self.grau = [-1] * num_nodes
        self.baix = [-1] * num_nodes
        self.en_pila = [False] * num_nodes
        self.pila = []
        self.components = []

    def afegir_aresta(self, origen, desti):
        self.graf[origen].append(desti)

    def tarjan(self, node):
        self.temps += 1
        self.grau[node] = self.temps
        self.baix[node] = self.temps
        self.pila.append(node)
        self.en_pila[node] = True

        for vei in self.graf[node]:
            if self.grau[vei] == -1:
                self.tarjan(vei)
                self.baix[node] = min(self.baix[node], self.baix[vei])
            elif self.en_pila[vei]:
                self.baix[node] = min(self.baix[node], self.grau[vei])

        if self.baix[node] == self.grau[node]:
            nova_component = []
            while True:
                u = self.pila.pop()
                self.en_pila[u] = False
                nova_component.append(u)
                if u == node:
                    break
            self.components.append(nova_component)

    def trobar_components_forts(self):
        for node in range(self.num_nodes):
            if self.grau[node] == -1:
                self.tarjan(node)
        return self.components

# Exemple d'ús
g = GrafDirigit(7)
g.afegir_aresta(0, 1)
g.afegir_aresta(1, 2)
g.afegir_aresta(2, 0)
g.afegir_aresta(1, 3)
g.afegir_aresta(1, 4)
g.afegir_aresta(3, 5)
g.afegir_aresta(4, 5)
g.afegir_aresta(5, 4)
g.afegir_aresta(6, 0)
g.afegir_aresta(6, 4)

components_forts = g.trobar_components_forts()
print(components_forts)
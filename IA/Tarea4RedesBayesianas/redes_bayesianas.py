from collections import defaultdict

class BayesianNetwork:
    def __init__(self, edges):
        """Inicializa la red bayesiana con una lista de aristas."""
        self.graph = defaultdict(set)
        self.build_graph(edges)

    def build_graph(self, edges):
        """Construye la red bayesiana a partir de una lista de aristas (pares padre-hijo)."""
        for parent, child in edges:
            self.graph[parent].add(child)
            self.graph[child].add(parent)

    def get_parents(self, node, directed_edges):
        """Devuelve los padres de un nodo en el grafo dirigido."""
        return [p for p, c in directed_edges if c == node]

    def find_paths(self, start, end, path=[]):
        """Encuentra todas las rutas posibles entre dos nodos."""
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.find_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def is_active_triple(self, X, Y, Z, evidence, directed_edges):
        """
        Verifica si la tripleta (X, Y, Z) esta activa dada la evidencia.
        """
        #Cadena causal X -> Y -> Z o causa comun X <- Y -> Z
        if (X in self.get_parents(Y, directed_edges) and Z not in self.get_parents(Y, directed_edges)) or \
           (Z in self.get_parents(Y, directed_edges) and X not in self.get_parents(Y, directed_edges)):
            if Y in evidence:
                return False  # Bloqueada- Y pertenece a la evidencia
            else:
                return True   # Activa- Y no pertenece a la evidencia

        #efecto comun X -> Y <- Z
        elif X in self.get_parents(Y, directed_edges) and Z in self.get_parents(Y, directed_edges):
            # Activa - Y o un descendiente pertenece a la evidencia
            descendants = self.find_descendants(Y, directed_edges)
            if Y in evidence or any(d in evidence for d in descendants):
                return True
            else:
                return False

        return False  # tripleta bloqueada

    def find_descendants(self, node, directed_edges):
        """Encuentra todos los descendientes de un nodo."""
        descendants = set()
        stack = [node]
        while stack:
            n = stack.pop()
            for parent, child in directed_edges:
                if parent == n and child not in descendants:
                    descendants.add(child)
                    stack.append(child)
        return descendants

    def d_separation(self, X, Z, evidence, directed_edges):
        """
        Verifica si X y Z estan D-separados dada la evidencia.
        """
        all_paths = self.find_paths(X, Z)  #rutas entre X y Z

        for path in all_paths:
            # Revisa cada tripleta en la ruta
            for i in range(len(path) - 2):
                X, Y, Z = path[i], path[i + 1], path[i + 2]
                if self.is_active_triple(X, Y, Z, evidence, directed_edges):
                    break  # tripleta activa - ruta activa
            else:
                return True  #nodos si son D-separados

        return False  #ruta es activa, los nodos no estan D-separados
    
    
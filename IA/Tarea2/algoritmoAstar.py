import heapq

class Astar:
    def __init__(self, inicio, meta, heuristica, grafo):
        """params
        inicio:     Nodo inicial
        meta:       Nodo meta
        heuristica: Costo estimado del camino mas barato
        grafo:      Definicion del problema en una estructura diccionario
        """
        self.inicio = inicio
        self.meta = meta
        self.heuristica = heuristica
        self.grafo = grafo
        
        #lista de probables vecinos
        self.lista_abierta = []
        #lista de elementos visitados
        self.lista_cerrada = set()
        heapq.heappush(self.lista_abierta, (0,inicio))
        #costo inicial 0
        self.costo_g = {inicio:0}
        #costo estimado
        self.costo_f = {inicio: heuristica[inicio]}
        #rastreo de nodos padres
        self.camino = {}
        
        
    def busquedaA(self):
        
        
        while self.lista_abierta:
            #Extrae el nodo con el menor costo estimado
            _, nodo_actual = heapq.heappop(self.lista_abierta)
            #print(f'{_} + {nodo_actual}')
            #verifica si es el nodo meta
            if nodo_actual==self.meta:
                return self.construir_solucion(nodo_actual)
            
            #coloca el nodo visitado en la lista cerrada
            self.lista_cerrada.add(nodo_actual)
            
            #explora el vecindario del nodo actual
            for vecino, costo in self.grafo[nodo_actual].items():
                #si el nodo ya fue visitado sigue con el siguiente vecino
                if vecino in self.lista_cerrada:
                    continue
                
                #se realiza la estimacion del costo f(x)
                costo_esperado =  self.costo_g[nodo_actual] + costo 
                
                #se evalua la estimacion del costo en cada vecino y si es el menor se considera 
                # en el camino solucion
                if vecino not in self.costo_g or costo_esperado < self.costo_g[vecino]:
                    self.camino[vecino] = nodo_actual
                    self.costo_g[vecino] = costo_esperado 
                    self.costo_f[vecino] = costo_esperado + self.heuristica[vecino]
                    #se añade el nodo en la lista abierta como posible estado siguiente
                    heapq.heappush(self.lista_abierta, (self.costo_f[vecino], vecino))
                    
        return None
    
    #funcion para la construccion de la solucion
    def construir_solucion(self, actual):
        camino = []
        #recorre la lista de los nodos almacenados 
        # para construir la solucion
        while actual in self.camino:
            camino.append(actual)
            actual = self.camino[actual]
        camino.append(self.inicio)
        #regresa el camino desde el nodo inicial al nodo meta
        return camino[::-1]
    
    
import algoritmoAstar as A

if __name__ == "__main__":
    
    # Definicion de grafo y heuristica
    mapa_romania  = {
        'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Zerind': {'Oradea': 71, 'Arad': 75},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj':  {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi':  {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87}
    }

    heuristica = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Fagaras': 176,
        'Rimnicu Vilcea': 193,
        'Pitesti': 100,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Bucharest': 0,
        'Giurgiu': 77,
        'Urziceni': 80,
        'Hirsova': 151,
        'Eforie': 161,
        'Vaslui': 199,
        'Iasi': 226,
        'Neamt': 234
    }

    # Crear instancia de la clase Astar
    algoritmo = A.Astar('Arad', 'Bucharest', heuristica, mapa_romania)
    camino = algoritmo.busquedaA()

    if camino:
        print("Camino encontrado:", " -> ".join(camino))
    else:
        print("No se encontro un camino.")
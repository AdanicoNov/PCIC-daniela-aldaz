import random

class BusquedaTabu:
        
    def __init__(self):
        self.n=0
    #Evaluacion de conflictos en tablero actual
    def is_solution(self, solucion):
        conflictos = 0
        n = len(solucion)
        for i in range(n):
            for j in range(i + 1, n):
                # Verificar misma columna o misma diagonal
                if solucion[i] == solucion[j] or abs(i - j) == abs(solucion[i] - solucion[j]):
                    conflictos += 1
        return conflictos

    #Generar posibles soluciones en el tablero
    def posible_solution(self, solucion):
        solutions = []
        n = len(solucion)
        # Generar vecinos (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                vecino = solucion[:]
                # Intercambiar las columnas de las reinas en las filas i y j
                vecino[i], vecino[j] = vecino[j], vecino[i]
                solutions.append(vecino)
        return solutions

    def tabu_search(self, ini_solution, max_iter, tamaño_tabu, tamaño_vecindario):
        # Inicializar la solución actual y la mejor solucion
        best_solution = ini_solution
        current_solution = ini_solution
        lista_tabu = []  # Lista tabu vacia
        mejor_valor = self.is_solution(best_solution)
        
        for iteracion in range(max_iter):
            # Generar vecindario de la solucion actual
            vecindario = self.posible_solution(current_solution)
            
            # Elegir la mejor solucion fuera de la lista tabu
            mejor_vecino = None
            mejor_valor_vecino = float('inf')
            
            for vecino in vecindario:
                if vecino not in lista_tabu:
                    #print(vecino)
                    valor_vecino = self.is_solution(vecino)
                    if valor_vecino < mejor_valor_vecino:
                        mejor_vecino = vecino
                        mejor_valor_vecino = valor_vecino
            
            # Aplicar criterios de aspiración
            if mejor_valor_vecino < mejor_valor:
                best_solution = mejor_vecino
                mejor_valor = mejor_valor_vecino
            
            # Actualizar la solucion actual y la lista tabu
            current_solution = mejor_vecino
            lista_tabu.append(current_solution)
            
            # Limitar el tamaño de la lista tabu
            if len(lista_tabu) > tamaño_tabu:
                lista_tabu.pop(0)  # Eliminar el movimiento más antiguo

        return best_solution, mejor_valor, lista_tabu

if __name__ == "__main__":
    # Número de reinas
    n = 4 
    solucion_ini = [random.randint(0, n - 1) for _ in range(n)]  # Solucion inicial aleatoria
    #print(solucion_ini)
    looking = BusquedaTabu()
    best_solution, conflictos, tabulist= looking.tabu_search( solucion_ini, 2000, 7, 200)

    print("Mejor solución encontrada:", best_solution)
    print("Conflictos en la mejor solución:", conflictos)
    print("Lista Tabu:", tabulist)

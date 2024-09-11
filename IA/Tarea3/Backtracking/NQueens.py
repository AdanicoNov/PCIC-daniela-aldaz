import numpy as np
import math
class NQueens:
    def __init__(self, n):
        #Tablero
        self.current_board = {}
        #Evary solution board
        self.all_boards = {}
        #posible positions
        #heapify para que los reordene conforme se reacomoden? Cuantos conflictos como restricciones
        self.positions = {}
        self.tam = n
        self.iter=0
        self.solutions = {}
        self.available_positions = {}
        
    def ordered_positions():
        #decribe conflict to the next positions
        print("ahorita")
            
    #filtering options    
    def is_option(self, new_option):
        for k in self.current_board:
            current_queen = self.current_board.values(k)
            print(f'current queen_i {self.current_board[k]}')
            abs_column = math.fabs(current_queen["i"] - new_option["i"])
            abs_row = math.fabs(current_queen["value"] - new_option["value"])

            # Misma fila o ataque diagonal
            if current_queen["value"] == new_option["value"] or abs_column == abs_row:
                return False  # Hay conflicto
        return True  # No hay conflicto

    
    def is_option_my(self, new_option):
        sol = True 
        conflict = 0
        for k in self.current_board:
            conflict = 0
            #como se conforma el tablero
            aver=self.current_board[k]["i"]
            #como se conforma la nueva opcion
            aver=new_option["i"]
            abs_column = math.fabs(self.current_board[k]["i"] - new_option["i"])
            abs_row = math.fabs(self.current_board[k]["value"] - new_option["value"])
            
            if self.current_board[k]["value"] == new_option["value"]:
                sol = False
                conflict +=1
                break
            
            if  abs_column == abs_row:
                sol = False
                conflict +=1
                break
        return sol
    
    def available_position(self, i):
        self.available_positions = {}
        nw_position = {}
        for k in range(self.tam):
            if (k not in self.current_board):
                nw_position = {"value":k,
                                "atack":0,
                                "i": i}
                #option = self.is_option_my(nw_position)
                #if option:
                self.available_positions[k]= nw_position
                #print(self.available_positions[k]["atack"])
                
    def print_positions(self):
        for  key, values in  self.available_positions.items():
            print(f"[{key}] [{values['value']}] ")  
            
        #de mayor a menor
        #valores_ord = dict(sorted(self.available_positions.items(), reverse=True))
        #print(valores_ord)
    def print_partial_solut(self):
        for  key, values in  self.current_board.items():
            print(f"[{key}] [{values['value']}] ")  
    
    def print_solutions(self):
        """ Imprimir todas las soluciones encontradas """
        for board in self.all_boards.items():
            for row in range(self.tam):
                line = ['_'] * self.tam
                print(row)
                line[board[row['value']]] = 'Q'
                print(' '.join(line))
            print("\n")
    
    def print_solution(self):
        """ Imprimir todas las soluciones encontradas """
        for element in self.current_board.items():
            print(self.current_board[element])
            #line = ['_'] * self.tam
            #line[element] = 'Q'
            #print(' '.join(line))
        print("\n")
          
            

if __name__ == "__main__":
    nwGame = NQueens(2)
    nwGame.available_position(0)
    print(nwGame.positions)
    nwGame.print_positions()
    
    option = nwGame.positions.get(1)
    print(option)
    isoption=nwGame.is_option(option)
    nwGame.positions.pop(1)
    print(isoption)
    nwGame.print_positions()
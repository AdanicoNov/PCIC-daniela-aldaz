
from Node import Node
import random 
import NQueens as NQ
class Backtracking:
    def __init__(self, n):
        self.n=n
    def recursiveBacktracking(self, i, p):
        """ 
        p: definition of the problem
        k: current iteration 
        """
        
        #La solucion es completa?
        if i == self.n:
            success = True
            p.all_boards[len(p.all_boards)] = p.current_board.copy()
                    
            return True
        
        success = False
        p.available_position(i)
        
        while p.available_positions:
            lst_avail_pos = list(p.available_positions.keys())
            
            new_option_key  = (list(p.available_positions.keys())[0])
            new_option = p.available_positions[new_option_key]
            #print(new_option)
            partial_sol = p.is_option_my(new_option)
            if partial_sol:
                
                p.current_board[i] = {'value':new_option['value'], 'i':i}
                p.print_partial_solut()
                #eliminar de la lista el valor newOption
                p.available_positions.pop(new_option_key)
                
                #llamar a la siguiente etapa de soluciones
                if self.recursiveBacktracking(i+1, problem):
                    return True
                p.available_positions[new_option_key] = new_option
                #Si en los niveles consecutivos no hay solucion, poda de rama
                p.current_board.pop(i)
                
            if p.available_positions.get(new_option_key) is not None:
                p.available_positions.pop(new_option_key)
        return success

    def solution(self, p):
        for i in range(p.tam):
            succe=self.recursiveBacktracking(i,p)
            print(succe)
if __name__ == "__main__":

    n = 8
    problem = NQ.NQueens(n)
    back_alg = Backtracking(n)
    sols = back_alg.solution(problem)
    problem.print_solutions()
    

import math
import MinMax
class TresEnLinea():
    def state(self, board):
        # Evaluar el estado actual del juego
        node_value = ''
        # Filas
        for fila in board:
            if fila[0] == fila[1] == fila[2] and fila[0] != ' ':
                if fila[0] == 'X':
                    node_value = 1
                else:
                    node_value =-1
                return node_value
            
        # Columnas
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                if board[0][col] == 'X':
                    node_value = 1
                else:
                    node_value = -1
                return node_value
                    
        # Diagonales
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            if board[0][0] == 'X':
                node_value = 1
            else:
                node_value = -1
            return node_value
        
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return 1 if board[0][2] == 'X' else -1
        
        #No hay ganador
        return 0

    def minimax(self, board, k, is_max):
        score = self.state(board)
        
        # El juego termino?
        if score == 1 or score == -1 or self.no_movements(board):
            return score
        
        # Si es el turno de maximizar
        if is_max:
            best_score = -math.inf
            for move in self.valid_movements(board):
                self.make_move(board, move, 'X')  # 'X' es el jugador que maximiza
                score = self.minimax(board, k + 1, False)
                self.undo_move(board, move)
                best_score = max(best_score, score)
            return best_score
        
        # Si es el turno de minimizar
        else:
            best_score = math.inf
            for move in self.valid_movements(board):
                self.make_move(board, move, 'O')  # 'O' es el jugador que minimiza
                score = self.minimax(board, k + 1, True)
                self.undo_move(board, move)
                best_score = min(best_score, score)
            return best_score

    def valid_movements(self, board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def make_move(self, board, move, jugador):
        i, j = move
        board[i][j] = jugador

    def undo_move(self, board, move):
        i, j = move
        board[i][j] = ' '

    def no_movements(self, board):
        for fila in board:
            if ' ' in fila:
                return False
        return True
    
    def mv_vs_mv(self, board):
        # Comienza jugador ('X')
        turno_maximizar = True 
        gato = TresEnLinea()

        while True:
            # Evaluar si el juego ha terminado
            evaluacion = gato.state(board)
            if evaluacion == 1:
                print("Jugador X (Maximiza) gana")
                break
            elif evaluacion == -1:
                print("Jugador O (Minimiza) gana")
                break
            elif gato.no_movements(board):
                print("Empate")
                break

            # Mostrar el board actual
            print("board actual:")
            for fila in board:
                print(fila)
            print()

            # Turno del jugador actual
            if turno_maximizar:
                print("Turno del jugador X (Maximiza)")
                best_move = None
                best_score = -math.inf
                for move in gato.valid_movements(board):
                    gato.make_move(board, move, 'X')
                    score = gato.minimax(board, 0, False)
                    gato.undo_move(board, move)
                    if score > best_score:
                        best_score = score
                        best_move = move
                gato.make_move(board, best_move, 'X')
            else:
                print("Turno del jugador O (Minimiza)")
                best_move = None
                best_score = math.inf
                for move in gato.valid_movements(board):
                    gato.make_move(board, move, 'O')
                    score = gato.minimax(board, 0, True)
                    gato.undo_move(board, move)
                    if score < best_score:
                        best_score = score
                        best_move = move
                gato.make_move(board, best_move, 'O')

            # Cambiar de turno
            turno_maximizar = not turno_maximizar


if __name__ == "__main__":
    tablero_inicial = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    gato = TresEnLinea()
    gato.mv_vs_mv(tablero_inicial)

from random import randint


class Solver:
    def __init__(self, board=None):
        self.__board = board

    @property
    def board(self):
        return self.__board
    

    def solve(self, board: list) -> bool:
        pos = self.next_pos(board)
        if not pos:
            return True
        for n in range(1, 10):
            if not self.exists(board, n, pos):
                board[pos[0]][pos[1]] = n
                if self.solve(board):
                    return True
                board[pos[0]][pos[1]] = 0
        return False

    def next_pos(self, board: list) -> tuple:
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return (r, c)
        return ()

    def exists(self, board: list, n: int, rc: tuple) -> tuple:
        for c in range(len(board)):
            if board[rc[0]][c] == n:
                return (rc[0], c)
        for r in range(len(board)):
            if board[r][rc[1]] == n:
                return (r, rc[1])
        spos = ((rc[0] // 3) * 3, (rc[1] // 3) * 3)
        for r in range(spos[0], spos[0] + 3):
            for c in range(spos[1], spos[1] + 3):
                if board[r][c] == n:
                    return (r, c)
        return ()

    
class Generator:
    def __init__(self):
        self.__solver = Solver()
        

    def generate(self, unempty) -> list:
        b = [[0 for r in range(9)] for c in range(9)]
        b[randint(0, 8)][randint(0, 8)] = randint(1, 9)
        ranpos = []
        
        counter = 1
        while counter <= unempty:
            r, c = randint(0, 8), randint(0, 8)
            if (r, c) not in ranpos:
                ranpos.append((r, c))
                counter += 1
        
        self.__solver.solve(b)
        b2 = [[] for i in range(9)]
        for r in range(9):
            for c in range(9):
                if (r, c) in ranpos:
                    b2[r].append(b[r][c])
                else:
                    b2[r].append(0)
        return b2

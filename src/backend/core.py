import cores

EMPTY = 0
WHITE = 1
BLACK = 2

class BoardData(object):
    def __init__(self):
        super(BoardData, self).__init__()
        self.current = EMPTY
        self.history = []

        self.board = []
        for i in range(0, 20):
            self.board.append([])
            for j in range(0, 20):
                self.board[-1].append(EMPTY)

    def is_in_range(self, i, j):
        return 1 <= i <= 19 and 1 <= j <= 19

    def get(self, i, j):
        return self.board[i][j]

    def set(self, i, j, chess):
        self.board[i][j] = chess


class Solver(object):
    def __init__(self, data):
        super(Solver, self).__init__()
        self.data = data

    def compute(self):
        return (1, 1)

import random

import cores

import imp
imp.reload(cores)

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

    def compute_one(self, i, j):
        return cores.judge(self.data, i, j)

    def compute(self):
        best = []
        for i in range(1, 20):
            for j in range(1, 20):
                score = self.compute_one(i, j)

                if len(best) == 0:
                    best.append((i, j, score))
                else:
                    if score > best[0][2]:
                        best = [(i, j, score)]
                    elif score == best[0][2]:
                        best.append((i, j, score))

        x, y, score = random.choice(best)
        return (x, y)

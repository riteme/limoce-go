import random
from collections import deque

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

    def reverse(self, color):
        return {
            EMPTY: EMPTY,
            WHITE: BLACK,
            BLACK: WHITE
        }[color]

    def is_dead(self, i, j):
        color = self.get(i, j)
        if color == EMPTY:
            return False

        q = deque()
        q.append((i, j))

        marked = set()

        while len(q) > 0:
            x, y = q.popleft()

            if not (x, y) in marked:
                marked.add((x, y))
            else:
                continue

            if not self.is_in_range(x, y):
                continue

            if self.get(x, y) == color:
                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))
            elif self.get(x, y) == EMPTY:
                return False

        return True

    def is_placable(self, i, j, color):
        if self.get(i, j) != EMPTY:
            return False

        self.set(i, j, color)
        result = self._is_placable(i, j, color)
        self.set(i, j, EMPTY)

        return result

    def _is_placable(self, i, j, color):
        neighbor = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1)
        ]
        for dx, dy in neighbor:
            cx = i + dx
            cy = j + dy
            if (self.is_in_range(cx, cy) and
                    self.get(cx, cy) == self.reverse(color) and
                    self.is_dead(cx, cy)):
                return True

        return not self.is_dead(i, j)

    def get_connected_component(self, i, j):
        color = self.get(i, j)
        result = []
        q = deque()
        q.append((i, j))

        marked = set()

        while len(q) > 0:
            x, y = q.popleft()

            if not (x, y) in marked:
                marked.add((x, y))
            else:
                continue

            if not self.is_in_range(x, y):
                continue

            if self.get(x, y) == color:
                result.append((x, y))
                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))

        return result

    def get_weak_doors(self, i, j):
        color = self.get(i, j)
        if color == EMPTY:
            return []

        result = []
        q = deque()
        q.append((i, j))

        marked = set()

        while len(q) > 0:
            x, y = q.popleft()

            if not (x, y) in marked:
                marked.add((x, y))
            else:
                continue

            if not self.is_in_range(x, y):
                continue

            if self.get(x, y) == color:
                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))
            elif self.get(x, y) == EMPTY:
                result.append((x, y))

        return result

    def get_doors(self, i, j):
        color = self.get(i, j)
        if color == EMPTY:
            return []

        result = []
        q = deque()
        q.append((i, j))

        marked = set()

        while len(q) > 0:
            x, y = q.popleft()

            if not (x, y) in marked:
                marked.add((x, y))
            else:
                continue

            if not self.is_in_range(x, y):
                continue

            if self.get(x, y) == color:
                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))
            elif self.get(x, y) == EMPTY:
                result.append((x, y))

                if self.is_in_range(x + 1, y) and self.get(x + 1, y) == color:
                    q.append((x + 1, y))
                if self.is_in_range(x - 1, y) and self.get(x - 1, y) == color:                
                    q.append((x - 1, y))
                if self.is_in_range(x, y + 1) and self.get(x, y + 1) == color:                
                    q.append((x, y + 1))
                if self.is_in_range(x, y - 1) and self.get(x, y - 1) == color:                
                    q.append((x, y - 1))

        return result


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

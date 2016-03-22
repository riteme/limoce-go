from defs import *

from collections import deque

UNIT_SCORE = -1500
SEARCH_SIZE = 20

def judge(data, x, y):
    count = 0
    friend_count = 0
    enemy_count = 0
    color = data.current
    q = deque()
    marked = set()
    q.append((x, y))

    while len(q) > 0 and count < SEARCH_SIZE:
        cx, cy = q.popleft()

        if not (cx, cy) in marked:
            marked.add((cx, cy))
        else:
            continue

        if not data.is_in_range(cx, cy):
            continue

        if data.get(cx, cy) == color:
            friend_count += 1
        elif data.get(cx, cy) == data.reverse(color):
            enemy_count += 1
        elif data.get(cx, cy) == EMPTY:
            q.append((cx + 1, cy))
            q.append((cx - 1, cy))
            q.append((cx, cy + 1))
            q.append((cx, cy - 1))

        count += 1

    if friend_count * 1.5 < enemy_count:
        return UNIT_SCORE * enemy_count
    return 0

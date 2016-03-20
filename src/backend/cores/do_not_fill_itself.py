from defs import *

from collections import deque

UNIT_SCORE = -20
SEARCH_SIZE = 15


def judge(data, x, y):
    count = 0
    color_count = 0
    color = data.get(x, y)
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
            color_count += 1
        elif data.get(cx, cy) == EMPTY:
            q.append((cx + 1, cy))
            q.append((cx - 1, cy))
            q.append((cx, cy + 1))
            q.append((cx, cy - 1))

        count += 1

    return color_count * UNIT_SCORE

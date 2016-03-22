from defs import *

UNIT_SCORE = -8000
DANGEROUS_LIMIT = 5

def fill_one(data, x, y):
    flag = True
    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dx, dy in directions:
        cx = x + dx
        cy = y + dy
        if data.is_in_range(cx, cy) and data.get(cx, cy) != data.current:
            flag = False

    if flag:
        return -100000
    else:
        return 0

def judge(data, x, y):
    score = fill_one(data, x, y)
    neighbor = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    origin = 0
    for dx, dy in neighbor:
        cx = x + dx
        cy = y + dy
        if data.is_in_range(cx, cy) and data.get(cx, cy) == data.current:
            doors = data.get_weak_doors(cx, cy)
            origin += len(doors)

    if origin > DANGEROUS_LIMIT:
        return score

    data.set(x, y, data.current)

    now = len(data.get_weak_doors(x, y))
    if now < origin:
        score += (origin - now) * UNIT_SCORE

    data.set(x, y, EMPTY)

    return score

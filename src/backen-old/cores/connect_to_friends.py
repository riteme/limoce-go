from defs import *

def neighbor(data, x, y):
    UNIT_SCORE = 150

    neighbors = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    count = 0
    for dx, dy in neighbors:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.current):
            count += 1

    return count * UNIT_SCORE

def small_jump(data, x, y):
    UNIT_SCORE = 200

    neighbors = [
        (-1, -1), (1, 1),
        (1,  -1), (-1,1)
    ]

    count = 0
    for dx, dy in neighbors:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.current):
            count += 1

    return count * UNIT_SCORE

def middle_jump(data, x, y):
    UNIT_SCORE = 150

    neighbors = [
        (1,  -2,  0, -1), (1,  2,  0, 1),
        (-1, -2,  0, -1), (-1, 2,  0, 1),
        (2,  -1,  1,  0), (2,  1,  1, 0),
        (-2, -1, -1,  0), (-2, 1, -1, 0),
        (0,   2,  0,  1), (0, -2,  0,-1),
        (2,   0,  1,  0), (-2, 0, -1, 0)
    ]

    count = 0
    for dx, dy, px, py in neighbors:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.current and
            data.get(x + px, y + py) == EMPTY):
            count += 1

    return count * UNIT_SCORE

def judge(data, x, y):
    situations = [
        neighbor,
        small_jump,
        middle_jump
    ]

    result = 0
    for sit in situations:
        result += sit(data, x, y)

    return result

def neighbor(data, x, y):
    UNIT_SCORE = 300

    neighbors = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    count = 0
    for dx, dy in neighbors:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.reverse(data.current)):
            count += 1

    return count * UNIT_SCORE

def small_jump(data, x, y):
    UNIT_SCORE = 275

    neighbors = [
        (-1, -1), (1, 1),
        (1,  -1), (-1,1)
    ]

    count = 0
    for dx, dy in neighbors:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.reverse(data.current)):
            count += 1

    return count * UNIT_SCORE

def middle_jump(data, x, y):
    UNIT_SCORE = 150

    neighbors = [
        (1,  -2), (1,  2),
        (-1, -2), (-1, 2),
        (2,  -1), (2,  1),
        (-2, -1), (-2, 1),
        (0,   2), (0, -2),
        (2,   0), (-2, 0)
    ]

    count = 0
    for dx, dy in neighbors:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.reverse(data.current)):
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

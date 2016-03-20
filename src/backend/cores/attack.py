from defs import *

SCORE_PER_CHESS = 1000


def judge(data, x, y):
    data.set(x, y, data.current)

    attacked = 0
    neighbor = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]
    for dx, dy in neighbor:
        cx = x + dx
        cy = y + dy
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.reverse(data.current) and
            data.is_dead(cx, cy)):
            attacked += len(
                data.get_connected_component(cx, cy)
            )

    data.set(x, y, EMPTY)

    return attacked * SCORE_PER_CHESS

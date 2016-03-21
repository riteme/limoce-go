import math

NEARBY_RADIUS = 5
UNIT_SCORE = 50


def judge(data, x, y):
    lx, ly, _ = data.history[-1]
    px = lx - x
    py = ly - y
    score = 0

    if abs(px) <= NEARBY_RADIUS and abs(py) <= NEARBY_RADIUS:
        score = abs(NEARBY_RADIUS - int(
            math.sqrt(px ** 2 + py ** 2)
        )) * UNIT_SCORE

    return score

NEARBY_RADIUS = 5
UNIT_SCORE = 10


def judge(data, x, y):
    lx, ly, _ = data.history[-1]
    px = lx - x
    py = ly - y
    score = 0

    if abs(px) <= NEARBY_RADIUS:
        score += abs(NEARBY_RADIUS - abs(px)) * UNIT_SCORE
    if abs(py) <= NEARBY_RADIUS:
        score += abs(NEARBY_RADIUS - abs(py)) * UNIT_SCORE

    return score

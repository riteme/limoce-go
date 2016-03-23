import random

from defs import *

UNIT_SCORE = 2000
CLIP_RADIUS = 1

def correct_bound(v):
    if v < 1:
        v = 1
    elif v > 19:
        v = 19

    return v

def get_clip(data, x, y):
    result = []
    left = correct_bound(x - CLIP_RADIUS)
    right = correct_bound(x + CLIP_RADIUS)
    top = correct_bound(y - CLIP_RADIUS)
    bottom = correct_bound(y + CLIP_RADIUS)

    for i in range(left, right + 1):
        for j in range(top,  bottom + 1):
            result.append(data.get(i, j))

    return result

def analyze(data):
    friend = data.current
    enemy = data.reverse(friend)
    my_count = 0
    enemy_count = 0

    for i in range(1, 20):
        for j in range(1, 20):
            clip = get_clip(data, i, j)
            black_count = clip.count(BLACK)
            white_count = clip.count(WHITE)
            status = None

            if black_count < white_count:
                status = WHITE
            elif black_count > white_count:
                status = BLACK
            else:
                status = EMPTY

            if status == friend:
                my_count += 1
            elif status == enemy:
                enemy_count += 1

    return (my_count, enemy_count)

def judge(data, x, y):
    origin_my, origin_enemy = analyze(data)

    if (x, y) == (1, 1):
        print("(debug) my: {}, enemy: {}".format(origin_my, origin_enemy))

    data.set(x, y, data.current)
    now_my, now_enemy = analyze(data)    
    data.set(x, y, EMPTY)

    return (
        (now_my - origin_my) * UNIT_SCORE -
        (origin_enemy - now_enemy) * UNIT_SCORE
    )

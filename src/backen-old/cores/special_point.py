from defs import *

SCORES = [
[-100,-100,-100, -100,-100,-100,-100,-100,-100, -100,-100,-100,-100,-100,-100, -100,-100,-100,-100],
[-100,  20,  20,   20,  20,  20,  20,  20,  20,   20,  20,  20,  20,  20,  20,   20,  20,  20,-100],
[-100,  20,  75,  100,  75,  40,  40,  40,  40,   75,  40,  40,  40,  40,  75,  100,  75,  20,-100],
[-100,  20, 100,99999, 100,  40,  40,  40,  75,99999,  75,  40,  40,  40, 100,99999, 100,  20,-100],
[-100,  20,  75,  100,  75,  40,  40,  40,  40,   75,  40,  40,  40,  40,  75,  100,  75,  20,-100],
[-100,  20,  40,   40,  40,  20,  20,  20,  20,   20,  20,  20,  20,  20,  40,   40,  40,  20,-100],
[-100,  20,  40,   40,  40,  20,   0,   0,   0,    0,   0,   0,   0,  20,  40,   40,  40,  20,-100],
[-100,  20,  40,   40,  40,  20,   0,   0,   0,    0,   0,   0,   0,  20,  40,   40,  40,  20,-100],
[-100,  20,  40,   75,  40,  20,   0,   0,   1,    5,   1,   0,   0,  20,  40,   75,  40,  20,-100],
[-100,  20,  75,99999,  75,  20,   0,   0,   5, 5000,   5,   0,   0,  20,  75,99999,  75,  20,-100],
[-100,  20,  40,   75,  40,  20,   0,   0,   1,    5,   1,   0,   0,  20,  40,   75,  40,  20,-100],
[-100,  20,  40,   40,  40,  20,   0,   0,   0,    0,   0,   0,   0,  20,  40,   40,  40,  20,-100],
[-100,  20,  40,   40,  40,  20,   0,   0,   0,    0,   0,   0,   0,  20,  40,   40,  40,  20,-100],
[-100,  20,  40,   40,  40,  20,  20,  20,  20,   20,  20,  20,  20,  20,  40,   40,  40,  20,-100],
[-100,  20,  75,  100,  75,  40,  40,  40,  40,   75,  40,  40,  40,  40,  75,  100,  75,  20,-100],
[-100,  20, 100,99999, 100,  40,  40,  40,  75,99999,  75,  40,  40,  40, 100,99999, 100,  20,-100],
[-100,  20,  75,  100,  75,  40,  40,  40,  40,   75,  40,  40,  40,  40,  75,  100,  75,  20,-100],
[-100,  20,  20,   20,  20,  20,  20,  20,  20,   20,  20,  20,  20,  20,  20,   20,  20,  20,-100],
[-100,-100,-100, -100,-100,-100,-100,-100,-100, -100,-100,-100,-100,-100,-100, -100,-100,-100,-100]
]

def judge(data, x, y):
    global SCORES

    return SCORES[x - 1][y - 1]

SCORES = [
[-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5],
[-5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -5],
[-5, 20, 75,100, 75, 40, 40, 40, 40, 75, 40, 40, 40, 40, 75,100, 75, 20, -5],
[-5, 20,100,600,100, 40, 40, 40, 75,300, 75, 40, 40, 40,100,600,100, 20, -5],
[-5, 20, 75,100, 75, 40, 40, 40, 40, 75, 40, 40, 40, 40, 75,100, 75, 20, -5],
[-5, 20, 40, 40, 40, 20, 20, 20, 20, 20, 20, 20, 20, 20, 40, 40, 40, 20, -5],
[-5, 20, 40, 40, 40, 20,  0,  0,  0,  0,  0,  0,  0, 20, 40, 40, 40, 20, -5],
[-5, 20, 40, 40, 40, 20,  0,  0,  0,  0,  0,  0,  0, 20, 40, 40, 40, 20, -5],
[-5, 20, 40, 75, 40, 20,  0,  0,  1,  5,  1,  0,  0, 20, 40, 75, 40, 20, -5],
[-5, 20, 75,300, 75, 20,  0,  0,  5,100,  5,  0,  0, 20, 75,300, 75, 20, -5],
[-5, 20, 40, 75, 40, 20,  0,  0,  1,  5,  1,  0,  0, 20, 40, 75, 40, 20, -5],
[-5, 20, 40, 40, 40, 20,  0,  0,  0,  0,  0,  0,  0, 20, 40, 40, 40, 20, -5],
[-5, 20, 40, 40, 40, 20,  0,  0,  0,  0,  0,  0,  0, 20, 40, 40, 40, 20, -5],
[-5, 20, 40, 40, 40, 20, 20, 20, 20, 20, 20, 20, 20, 20, 40, 40, 40, 20, -5],
[-5, 20, 75,100, 75, 40, 40, 40, 40, 75, 40, 40, 40, 40, 75,100, 75, 20, -5],
[-5, 20,100,600,100, 40, 40, 40, 75,300, 75, 40, 40, 40,100,600,100, 20, -5],
[-5, 20, 75,100, 75, 40, 40, 40, 40, 75, 40, 40, 40, 40, 75,100, 75, 20, -5],
[-5, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, -5],
[-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]
]

def judge(data, x, y):
    global SCORES

    return SCORES[x - 1][y - 1]
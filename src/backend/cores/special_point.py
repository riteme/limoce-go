SCORES = [
[-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5],
[-5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -5],
[-5, 10, 25, 50, 25, 20, 20, 20, 20, 25, 20, 20, 20, 20, 25, 50, 25, 10, -5],
[-5, 10, 50, 70, 50, 20, 20, 20, 25, 50, 25, 20, 20, 20, 50, 70, 50, 10, -5],
[-5, 10, 25, 50, 25, 20, 20, 20, 20, 25, 20, 20, 20, 20, 25, 50, 25, 10, -5],
[-5, 10, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 10, -5],
[-5, 10, 20, 20, 20, 10,  0,  0,  0,  0,  0,  0,  0, 10, 20, 20, 20, 10, -5],
[-5, 10, 20, 20, 20, 10,  0,  0,  0,  0,  0,  0,  0, 10, 20, 20, 20, 10, -5],
[-5, 10, 20, 25, 20, 10,  0,  0,  1,  5,  1,  0,  0, 10, 20, 25, 20, 10, -5],
[-5, 10, 25, 50, 25, 10,  0,  0,  5, 10,  5,  0,  0, 10, 25, 50, 25, 10, -5],
[-5, 10, 20, 25, 20, 10,  0,  0,  1,  5,  1,  0,  0, 10, 20, 25, 20, 10, -5],
[-5, 10, 20, 20, 20, 10,  0,  0,  0,  0,  0,  0,  0, 10, 20, 20, 20, 10, -5],
[-5, 10, 20, 20, 20, 10,  0,  0,  0,  0,  0,  0,  0, 10, 20, 20, 20, 10, -5],
[-5, 10, 20, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 10, -5],
[-5, 10, 25, 50, 25, 20, 20, 20, 20, 25, 20, 20, 20, 20, 25, 50, 25, 10, -5],
[-5, 10, 50, 70, 50, 20, 20, 20, 25, 50, 25, 20, 20, 20, 50, 70, 50, 10, -5],
[-5, 10, 25, 50, 25, 20, 20, 20, 20, 25, 20, 20, 20, 20, 25, 50, 25, 10, -5],
[-5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, -5],
[-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5, -5]
]

def judge(data, x, y):
    global SCORES

    return SCORES[x - 1][y - 1]

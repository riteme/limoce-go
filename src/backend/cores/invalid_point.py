import defs

def judge(data, x, y):
    if data.get(x, y) != defs.EMPTY:
        return -1000000
    return 0

INFTY_MIN = -100000000

def judge(data, x, y):
    if not data.is_placable(x, y, data.current):
        return INFTY_MIN
    return 0

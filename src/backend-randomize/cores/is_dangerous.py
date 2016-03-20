UNIT_SCORE = -1000
DANGEROUS_LIMIT = 1

def judge(data, x, y):
    data.set(x, y, data.current)

    doors = data.get_weak_doors(x, y)
    if len(doors) <= DANGEROUS_LIMIT:
        return UNIT_SCORE

    return 0

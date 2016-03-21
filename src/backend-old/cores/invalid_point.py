INFTY_MIN = -100000000

def judge(data, x, y):
    if not data.is_placable(x, y, data.current):
        return INFTY_MIN

    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]
            
    neighbors = [(x - dx, y - dy) for dx, dy in directions]
    status = []
    color = data.current
    enemy = data.reverse(data.current)
    for cx, cy in neighbors:
        if not data.is_in_range(cx, cy):
            status.append(enemy)
        elif data.get(cx, cy) == enemy:
            status.append(enemy)
        else:
            status.append(color)

    if status == [enemy for i in range(0, 4)]:
        # print("(debug) Forbidden")
        # print("(debug) last: {}".format(data.history[-1][:2]))
        if data.history[-1][:2] in neighbors:
            return INFTY_MIN

    return 0

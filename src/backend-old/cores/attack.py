from defs import *

SCORE_PER_CHESS = 150000
UNIT_SCORE = 5000
DANGEROUS_LIMIT = 4
DANGEROUS_SCORE = 10000

def judge(data, x, y):
    score = 0
    attacked = 0
    neighbor = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]
    for dx, dy in neighbor:
        cx = x + dx
        cy = y + dy

        data.set(x, y, data.current)
        if (data.is_in_range(cx, cy) and
            data.get(cx, cy) == data.reverse(data.current)):
            if data.is_dead(cx, cy):
                attacked += len(
                    data.get_connected_component(cx, cy)
                )
            else:
                door_number = len(data.get_weak_doors(cx, cy))
                data.set(x, y, EMPTY)
                origin_door_number = len(data.get_weak_doors(cx, cy))

                data.set(x, y, data.current)
                if door_number < origin_door_number and len(data.get_weak_doors(x, y)) > 1:
                    score += (origin_door_number - door_number) * UNIT_SCORE

                    if door_number <= DANGEROUS_LIMIT:
                        offest = DANGEROUS_LIMIT - door_number + 1
                        score += offest * DANGEROUS_SCORE
                    
        data.set(x, y, EMPTY)

    return attacked * SCORE_PER_CHESS + score

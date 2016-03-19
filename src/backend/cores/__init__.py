import imp

import cores.invalid_point
import cores.randomize
import cores.special_point

print("(info) Core modules is loading...")

judgers = []

def add_judger(func):
    global judgers

    judgers.append(func)

def judge(data, x, y):
    global judgers

    result = 0
    for judger in judgers:
        result += judger(data, x, y)

    return result


imp.reload(cores.invalid_point)
add_judger(cores.invalid_point.judge)

imp.reload(cores.randomize)
add_judger(cores.randomize.judge)

imp.reload(cores.special_point)
add_judger(cores.special_point.judge)

print("(info) Core modules loaded.")

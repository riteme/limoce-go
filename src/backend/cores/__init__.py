import imp

import cores.invalid_point
import cores.randomize
import cores.special_point
import cores.attack

components = [
    cores.invalid_point,
    cores.randomize,
    cores.randomize,
    cores.attack
]

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

        # if the score is too low
        if result < -9000000:
            break

    return result

for module in components:
    imp.reload(module)
    add_judger(module.judge)

print("(info) Core modules loaded.")

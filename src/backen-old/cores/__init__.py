import imp

import cores.invalid_point
import cores.special_point
import cores.do_not_fill_itself
import cores.do_not_kill_friends
import cores.save_friends
import cores.connect_to_friends
import cores.connect_to_enemy
import cores.all_is_enemy
import cores.is_dangerous
import cores.attack
import cores.nearby
import cores.analyze
import cores.randomize

components = [
    cores.invalid_point,
    cores.special_point,
    cores.do_not_fill_itself,
    cores.do_not_kill_friends,
    cores.save_friends,
    cores.connect_to_friends,
    cores.connect_to_enemy,
    cores.all_is_enemy,
    cores.is_dangerous,
    cores.attack,
    cores.nearby,
    cores.analyze,
    cores.randomize
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

        # if (x, y) == (5, 2):
        #     print("(debug) {}".format(result))

        # if the score is too low
        if result < -9000000:
            break

    return result

for module in components:
    imp.reload(module)
    add_judger(module.judge)

print("(info) Core modules loaded.")

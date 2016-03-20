import core

from config import *

def parse_data(data):
    result = core.BoardData()

    symbols = {
        EMPTY_CHAR: core.EMPTY,
        WHITE_CHAR: core.WHITE,
        BLACK_CHAR: core.BLACK
    }

    offest = 0

    if PARSE_CURRENT:
        if data[offest] == WHITE_CURRENT:
            result.current = core.WHITE
        elif data[offest] == BLACK_CURRENT:
            result.current = core.BLACK
        else:
            raise RuntimeError(
                "Error when parsing current chess:\n" +
                "Unexcepted char: {}".format(data[offest])
            )

        offest += 1

    if PARSE_BOARD:
        for i in range(1, 20):
            for j in range(1, 20):
                chess = symbols[data[offest]]

                result.set(j, i, chess)

                offest += 1

    if PARSE_HISTORY:
        for i in range(offest, len(data), 3):
            i, j, chess = (
                ord(data[offest]), ord(data[offest + 1]),
                symbols[data[offest + 2]]
            )

            if chess == core.EMPTY:
                raise ValueError(
                    "Invalid history: {}, {}: {}".format(i, j, chess)
                )

            result.history.append((j, i, chess))

    return result

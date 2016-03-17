from collections import deque

from defs import *

from sfml import *

NONE = Color.TRANSPARENT
WHITE = Color.WHITE
BLACK = Color.BLACK

board_grid = None
circles = None
chesses = {}

offest_x = 0
offest_y = 0

def reverse(color):
    global NONE
    global WHITE
    global BLACK

    if color == NONE:
        return NONE
    elif color == WHITE:
        return BLACK
    elif color == BLACK: 
        return WHITE

def is_inside_board(px, py):
    global offest_x
    global offest_y

    px -= offest_x
    py -= offest_y

    return (
        0 <= px and px <= 38 * BLOCK_RADIUS and
        0 <= py and py <= 38 * BLOCK_RADIUS
    )

def to_index(px, py):
    global offest_x
    global offest_y

    px -= offest_x
    py -= offest_y

    return (int(px / (2 * BLOCK_RADIUS)) + 1, int(py / (2 * BLOCK_RADIUS)) + 1)

def to_position(x, y, radius = CHESS_RADIUS):
    return (
        offest_x + (2 * x - 1) * BLOCK_RADIUS - radius,
        offest_y + (2 * y - 1) * BLOCK_RADIUS - radius
    )

def is_dead(i, j):
    global NONE
    global WHITE
    global BLACK

    color = get_chess(i, j)
    q = deque()
    q.append((i, j))

    while len(q) > 0:
        x, y = q[0]
        q.popleft()

        if 1 <= x and x <= 19 and 1 <= y and y <= 19:
            if get_chess(x, y) == NONE:
                return False
            elif get_chess(x, y) == color:
                q.append((x - 1, y))
                q.append((x + 1, y))
                q.append((x, y - 1))
                q.append((x, y + 1))                

    return True

def is_placable(i, j, color):
    global chesses
    global NONE
    global WHITE
    global BLACK

    if not (i, j) in chesses:
        return True

    return False

def prepare_board(_offest_x = 0, _offest_y = 0):
    global board_grid
    global circles

    global offest_x
    global offest_y
    offest_x = _offest_x
    offest_y = _offest_y

    board_grid = VertexArray(PrimitiveType.LINES)
    for i in range(0, 19):
        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS, 
                    offest_y + BLOCK_RADIUS
                ), Color.BLACK
            )
        )

        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS,
                    offest_y + BLOCK_RADIUS + 36 * BLOCK_RADIUS
                ), Color.BLACK
            )
        )

        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS,
                    offest_y + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS
                ), Color.BLACK
            )
        )

        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS + 36 * BLOCK_RADIUS,
                    offest_y + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS
                ), Color.BLACK
            )
        )

    circles = []

    POSITIONS = [
        (3, 3), (3, 9), (3, 15),
        (9, 3), (9, 9), (9, 15),
        (15, 3), (15, 9), (15, 15)
    ]

    for point in POSITIONS:
        x, y = point

        circle = CircleShape(point_count = CIRCLE_POINTS_NUMBER)
        circle.radius = POINT_RADIUS
        circle.fill_color = Color.BLACK
        circle.position = (
            offest_x + BLOCK_RADIUS * 2 * x + BLOCK_RADIUS - POINT_RADIUS,
            offest_y + BLOCK_RADIUS * 2 * y + BLOCK_RADIUS - POINT_RADIUS
        )

        circles.append(circle)

def get_chess(x, y):
    global chesses
    global NONE
    global WHITE
    global BLACK

    if not (x, y) in chesses:
        return NONE

    return chesses[(x, y)].fill_color

def set_chess(x, y, color):
    global chesses
    global offest_x
    global offest_y

    global NONE
    global WHITE
    global BLACK

    if color == NONE:
        if (x, y) in chesses:
            chesses.pop((x, y))
            return

    chess = CircleShape(point_count = CIRCLE_POINTS_NUMBER)
    chess.radius = CHESS_RADIUS
    chess.position = (
        offest_x + (2 * x - 1) * BLOCK_RADIUS - CHESS_RADIUS,
        offest_y + (2 * y - 1) * BLOCK_RADIUS - CHESS_RADIUS
    )
    chess.fill_color = color

    chesses[(x, y)] = chess

def render_board(window):
    global board_grid
    global circles

    window.draw(board_grid)

    for circle in circles:
        window.draw(circle)

def render_chess(window):
    for chess in chesses.values():
        window.draw(chess)

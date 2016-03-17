import copy

import board

from defs import *

from sfml import *

current_block = RectangleShape()
current_block.size = (BLOCK_RADIUS * 2, BLOCK_RADIUS * 2)
current_block.position = (INVALID_X, INVALID_Y)
current_block.fill_color = CURRENT_SELECT_COLOR

current_color = board.BLACK

current_chess = CircleShape(point_count = CIRCLE_POINTS_NUMBER)
current_chess.position = (CURRENT_CHESS_X, CURRENT_CHESS_Y)
current_chess.radius = CURRENT_CHESS_RADIUS

current_count = 1

default_font = Font.from_file(FONT)

history = []
history_text = Text()
history_text.font = default_font
history_text.character_size = HISTORY_TEXT_SIZE
history_text.color = HISTORY_TEXT_COLOR
history_text.position = (HISTORY_TEXT_X, HISTORY_TEXT_Y)

old_history = []

def undo():
    global current_color
    global old_history
    global history
    global current_count

    if len(old_history) > 0:
        chess_data, history = old_history.pop()
        restore_board(chess_data)
        current_count -= 1

        update_history_text()

        current_color = board.reverse(current_color)

def copy_board():
    result = []

    for key, value in board.chesses.items():
        x, y = key
        color = value.fill_color

        result.append((x, y, color))

    return result

def restore_board(data):
    board.chesses = {}

    for x, y, color in data:
        board.set_chess(x, y, color)

def backup():
    global old_history
    global history

    old_history.append((
        copy_board(), copy.deepcopy(history)
    ))

def update_history_text():
    global history_text
    global history

    history_text.string = "\n".join(history)

def update_history(i, j):
    global current_color
    global current_count
    global history
    global history_text

    color_name = "W"
    if current_color == board.BLACK:
        color_name = "B"

    history.append("{:>3} {} {:<3} {:<2}".format(
        current_count, color_name, str(i) + ",", j)
    )

    if len(history) > HISTORY_TEXT_MAX_LINES:
        history.pop(0)
    
    update_history_text()

    current_count += 1

def update_chess(i, j):
    color = board.get_chess(i, j)
    enemy = board.reverse(color)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        x = i + dx
        y = j + dy
        if board.is_in_range(x, y) and board.get_chess(x, y) == enemy:
            if board.is_dead(x, y):
                board.clear_block(x, y)

def place_chess(i, j):
    global current_color
    global old_history
    global current_count
    global history

    if board.get_chess(i, j) != board.NONE:
        return

    backup()

    board.set_chess(i, j, current_color)
    if not board.is_placable(i, j, current_color):
        board.set_chess(i, j, board.NONE)
        return

    update_history(i, j)
    update_chess(i, j)

    current_color = board.reverse(current_color)

def do_events(window):
    global current_color
    global history

    for event in window.events:
        if type(event) is CloseEvent:
            window.close()

        elif type(event) is KeyEvent:
            if event.released:
                if event.code == Keyboard.ESCAPE:
                    window.close()
                elif event.code == Keyboard.Z:
                    undo()

        elif type(event) is MouseMoveEvent:
            if not board.is_inside_board(event.position.x, event.position.y):
                continue

            i, j = board.to_index(event.position.x, event.position.y)
            current_block.position = board.to_position(i, j, BLOCK_RADIUS)

        elif type(event) is MouseButtonEvent:
            if not board.is_inside_board(event.position.x, event.position.y):
                continue

            if event.pressed:
                continue

            i, j = board.to_index(event.position.x, event.position.y)
            place_chess(i, j)

if __name__ == "__main__":
    setting = ContextSettings()
    setting.antialiasing_level = WINDOW_ANTIALIAS

    window = RenderWindow(
        VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_TITLE,  WINDOW_STYLE,
        settings = setting
    )

    board.prepare_board(OFFEST_X, OFFEST_Y)

    while window.is_open:
        do_events(window)

        window.clear(WINDOW_BACKGROUND_COLOR)

        board.render_board(window)
        window.draw(current_block)
        board.render_chess(window)

        current_chess.fill_color = current_color
        window.draw(current_chess)

        window.draw(history_text)

        window.display()

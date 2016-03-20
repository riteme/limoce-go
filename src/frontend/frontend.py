import sys
import imp
import copy
import socket
import threading

import board
import config

from defs import *

from sfml import *

last_x = 0
last_y = 0

last_block = RectangleShape()
last_block.size = (BLOCK_RADIUS * 2, BLOCK_RADIUS * 2)
last_block.position = (INVALID_X, INVALID_Y)
last_block.fill_color = Color.TRANSPARENT
last_block.outline_color = LAST_PLACED_COLOR
last_block.outline_thickness = LAST_PLACED_THICKNESS

current_block = RectangleShape()
current_block.size = (BLOCK_RADIUS * 2, BLOCK_RADIUS * 2)
current_block.position = (INVALID_X, INVALID_Y)
current_block.fill_color = CURRENT_SELECT_COLOR

current_color = board.BLACK

current_chess = CircleShape(point_count=CIRCLE_POINTS_NUMBER)
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
    global last_block
    global last_x
    global last_y

    if len(old_history) > 0:
        chess_data, history, last_x, last_y = old_history.pop()
        restore_board(chess_data)
        current_count -= 1

        update_history_text()
        last_block.position = board.to_position(last_x, last_y, BLOCK_RADIUS)

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
    global last_x
    global last_y

    old_history.append((
        copy_board(), copy.deepcopy(history), last_x, last_y
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
    global last_block
    global last_x
    global last_y

    if board.get_chess(i, j) != board.NONE:
        print("(warn) Can't place at {}, {}".format(
            i, j    
        ))
        return

    board.set_chess(i, j, current_color)
    if not board.is_placable(i, j, current_color):
        board.set_chess(i, j, board.NONE)
        print("(warn) Can't place at {}, {}".format(
            i, j    
        ))
        return

    board.set_chess(i, j, board.NONE)
    backup()

    board.set_chess(i, j, current_color)

    update_history(i, j)
    update_chess(i, j)
    last_block.position = board.to_position(i, j, BLOCK_RADIUS)
    last_x = i
    last_y = j

    current_color = board.reverse(current_color)


def make_board_data():
    global current_color
    global last_x
    global last_y

    def symbols(color):
        if color == board.WHITE:
            return "W"
        elif color == board.BLACK:
            return "B"
        else:
            return "+"
    buf = [symbols(current_color)]

    for i in range(1, 20):
        for j in range(1, 20):
            buf.append(symbols(
                board.get_chess(i, j)
            ))

    buf.append(chr(last_x))
    buf.append(chr(last_y))
    buf.append(symbols(board.reverse(current_color)))

    return "".join(buf)


def furthur_require():
    try:
        imp.reload(config)
        host = config.SERVER_HOST
        port = config.SERVER_PORT

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        data = make_board_data().encode("ascii")
        sock.send(data)

        reply = sock.recv(256)
        x, y = (reply[0], reply[1])
        place_chess(x, y)

    except Exception as e:
        print("(error) An exception occurred when ask for furthur server:\n{}".format(
            str(e)
        ))


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
                elif event.code == Keyboard.Q:
                    thread = threading.Thread(
                        target=furthur_require
                    )
                    thread.run()

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
        settings=setting
    )

    board.prepare_board(OFFEST_X, OFFEST_Y)

    while window.is_open:
        do_events(window)

        window.clear(WINDOW_BACKGROUND_COLOR)

        board.render_board(window)
        window.draw(current_block)
        board.render_chess(window)
        window.draw(last_block)

        current_chess.fill_color = current_color
        window.draw(current_chess)

        window.draw(history_text)

        window.display()

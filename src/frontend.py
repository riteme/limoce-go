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

default_font = Font.from_file(FONT)

history = []
history_text = Text()
history_text.font = default_font
history_text.character_size = HISTORY_TEXT_SIZE
history_text.color = HISTORY_TEXT_COLOR
history_text.position = (HISTORY_TEXT_X, HISTORY_TEXT_Y)

def place_chess(i, j):
    global current_color
    global history
    global history_text

    board.set_chess(i, j, current_color)

    color_name = "White"
    if current_color == board.BLACK:
        color_name = "Black"
    history.append("{}: {:<3} {:<2}".format(color_name, str(i) + ",", j))
    if len(history) > HISTORY_TEXT_MAX_LINES:
        history.pop(0)
    history_text.string = "\n".join(history)

    current_color = board.reverse(current_color)

def do_events(window):
    global current_color

    for event in window.events:
        if type(event) is CloseEvent:
            window.close()

        elif type(event) is KeyEvent:
            if event.released:
                if event.code == Keyboard.ESCAPE:
                    window.close()

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

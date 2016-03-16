import board

from defs import *

from sfml import *

current_block = RectangleShape()
current_block.size = (BLOCK_RADIUS * 2, BLOCK_RADIUS * 2)
current_block.position = (INVALID_X, INVALID_Y)
current_block.fill_color = CURRENT_SELECT_COLOR

current = board.BLACK

def do_events(window):
    global current

    for event in window.events:
        if type(event) is CloseEvent:
            window.close()

        elif type(event) is KeyEvent:
            if event.released:
                if event.code == Keycode.ESCAPE:
                    window.close()

        elif type(event) is MouseMoveEvent:
            i, j = board.to_index(event.position.x, event.position.y)
            current_block.position = board.to_position(i, j, BLOCK_RADIUS)

        elif type(event) is MouseButtonEvent:
            if event.pressed:
                continue

            i, j = board.to_index(event.position.x, event.position.y)
            board.set_chess(i, j, current)

            current = board.reverse(current)

if __name__ == "__main__":
    window = RenderWindow(VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_TITLE,  WINDOW_STYLE)

    board.prepare_board()

    board.set_chess(1, 1, board.WHITE)
    board.set_chess(2, 1, board.BLACK)
    board.set_chess(3, 1, board.WHITE)

    while window.is_open:
        do_events(window)

        window.clear(Color(205, 154, 61))

        board.render_board(window)
        window.draw(current_block)
        board.render_chess(window)

        window.display()

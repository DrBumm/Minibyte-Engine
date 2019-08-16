# Movement

import time
from src import ca, gtps


def _find_getch():
    try:
        import termios
    except ImportError:
        # Non-POSIX. Return msvcrt's (Windows') getch.
        import msvcrt
        return msvcrt.getch

    # POSIX system. Create and return a getch that manipulates the tty.
    import sys
    import tty

    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch


def mv(lvl, done=False):
    getch = _find_getch()
    while not done:
        key = getch()
        # print(key)
        if key != '':
            if key == b'a':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'l', lvl)
            if key == b'd':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'r', lvl)
            if key == b'w':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'u', lvl)
            if key == b's':
                done = True
                return ca.move(gtps.get_player_pos(lvl), 'd', lvl)
            if key == b'\x03':
                print('Exiting')
                time.sleep(3)
                exit()
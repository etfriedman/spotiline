import time
import curses


stdscr = curses.initscr()

curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

stdscr.addstr(5, 10, "Hello, world!")

stdscr.refresh()

time.sleep(3)

stdscr.clear()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()

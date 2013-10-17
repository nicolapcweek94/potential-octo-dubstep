#!/usr/bin/env python
import curses, os

def main(stdscr):
    path = '/home/wasp/'
    stdscr.clear()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    i = 0
    offset = 0
    selected = 0
 
    while True:
        stdscr.clear()

        for f in os.listdir(path)[offset:]:
            if i == selected:
                stdscr.addstr(i, 0, f, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, f)
            i = i + 1
            if i == curses.LINES:
                break
        i = 0
        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_UP:
            if selected == 0:
                if offset != 0:
                    offset = offset - 1
            else:
                selected = selected - 1
        
        elif key == curses.KEY_DOWN:
            if selected == curses.LINES - 1:
                if offset != len(os.listdir(path)) - curses.LINES:
                    offset = offset + 1
            elif selected < len(os.listdir(path)) - 1:
                selected = selected + 1
        
        elif chr(key) == '\n':
            path = path + os.listdir(path)[offset + selected] + '/'
            selected = 0
            offset = 0
        
        elif key == ord('q'):
            break

curses.wrapper(main)

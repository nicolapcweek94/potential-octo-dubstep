#!/usr/bin/env python
import curses, os, os.path

def main(stdscr):
    path = '/home/wasp/'
    i = 0
    offset = 0
    selected = 0
    ls = []
    ldir = []
    lfile = []

    stdscr.clear()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    for f in os.listdir(path):
        if os.path.isdir(path + f):
            ldir.append(f)
        else:
            lfile.append(f)

    while True:
        stdscr.clear()
        
        ls = sorted(ldir) + sorted(lfile)

        for f in ls[offset:]:
            if i == selected:
                stdscr.addstr(i, 0, f, curses.A_REVERSE)
            elif os.path.isdir(path + f):
                stdscr.addstr(i, 0, f, curses.color_pair(1))
            elif os.path.isfile(path + f):
                stdscr.addstr(i, 0, f, curses.color_pair(2))
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
                if offset != len(ls) - curses.LINES:
                    offset = offset + 1
            elif selected < len(ls) - 1:
                selected = selected + 1
        
        elif chr(key) == '\n':
            path = path + ls[offset + selected] + '/'
            selected = 0
            offset = 0
            ldir = []
            lfile = []

            for f in os.listdir(path):
                if os.path.isdir(path + f):
                    ldir.append(f)
                else:
                    lfile.append(f)
                            
        
        elif key == ord('q'):
            break

curses.wrapper(main)

'''
The Salt Console, this system is used to display a curses console that posts
event and job data as it happens from within Salt
'''

# Import python libs
import curses

# Import salt libs
import salt.utils.event


class SaltConsole(object):
    '''
    '''
    def __init__(self, opts):
        self.opts = opts
        self.scr = curses.initscr()
        self.event = salt.utils.event()
        self.__setup_screen()

    def __setup_screen(self):
        '''
        '''
        # Prep Curses
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        # Prep the screen
        self.scr.keypad(1)
        self.scr.box()
        self.scr.addstr(1, 1, 'Salt Console')
        self.scr.addstr(1, 2, '='*34)
        # Turn it all on!
        self.scr.refresh()

    def term(self):
        '''
        '''
        curses.curs_set(1)
        curses.nocbreak()
        self.scr.keypad(0)
        curses.echo()
        curses.endwin()


    def run(self):
        '''
        '''
        while True:
            try:
                pass
            except Exception:
                self.term()

if __name__ == '__main__':
    console = SaltConsole()
    console.run()


import sys, time

class Main:
    def __init__(self, action=None) -> None:
        if action is None: self.r = None
        else:
            if action == 'import.error': self.import_err()
            elif action == 'open.error': self.open_err()
            elif action == 'load.error': self.load_error()
    def quit(self):
        time.sleep(self.time) if self.time is not None else time.sleep(2)
        sys.exit()
    def import_err(self): print(' Please install all the packages (open a console and type pip install -r /path/to/requirements.txt)'); self.r = True; self.quit()
    def open_err(self): print(' The filename you entered is not valid, please re-try with another file'); self.r = True; self.quit()
    def load_error(self): print(' Error while loading your lines. Try again later.'); self.r = True; self.quit()
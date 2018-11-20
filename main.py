from display import *
from msgbox import *


class XO():
    def main(self):
        self.end=False
        while not self.end:
            self.gui = Gui()
            self.gui.start()
            self.gui.init(self)
            self.gui.join()


obj = XO()
obj.main()

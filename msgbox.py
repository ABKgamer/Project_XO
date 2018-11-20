from tkinter import *
from threading import *


class Mb(Thread):
    def run(self, obj, titlemsg="Message Box" ,lablemsg="sample Text", leftbuttonmsg="left", rightbuttonmsg="right"):
        self.mainobj =obj
        self.player=None
        self.gui = Tk()
        self.gui.title(titlemsg)
        self.lab = Label(self.gui, text=lablemsg)
        self.lab.grid(columnspan=2, row=0)
        self.butleft = Button(self.gui, text=leftbuttonmsg, command=self.leftclick)
        self.butleft.grid(row=1,column=0)
        self.butright = Button(self.gui, text=rightbuttonmsg, command=self.rightclick)
        self.butright.grid(row=1,column=1)
        self.gui.resizable(width=False, height=False)
        self.gui.mainloop()

    def leftclick(self):
        self.mainobj.player = "X"
        self.gui.quit()

    def rightclick(self):
        self.mainobj.player = "O"
        self.gui.quit()


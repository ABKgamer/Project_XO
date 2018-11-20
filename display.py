from comp import *
from msgbox import *
from tkinter import *
from threading import *


class Gui(Thread):
    def init(self,obj):
        self.mobj = obj
        self.lis = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
        self.moves = []
        self.moves.clear()
        self.gOB = []
        self.gOB.clear()
        self.player = " "
        self.turn = "X"
        self.won = ""
        self.count = 1
        self.comp_obj = AI(self)
        self.comp_obj.getpossiblexo()
        self.choce()

    def run(self):
        self.gui = Tk()
        self.setbut()
        self.gui.resizable(width=False,height=False)
        self.gui.mainloop()

    def setbut(self):
        for x in range(0, 3):
            temp = []
            temp.clear()
            for y in range(0, 3):
                if self.lis[x][y]=="X":
                    temp.append(Button(self.gui, text="X"))
                if self.lis[x][y]=="O":
                    temp.append(Button(self.gui, text="O"))
                else:
                    temp.append(Button(self.gui, text=" ", command=lambda tval = int(str(x+1)+str(y+1)): self.butfun(args=tval)))
            self.gOB.append(temp)
        for x in range(0, 3):
            for y in range(0, 3):
                self.gOB[x][y].grid(row=x,column=y)
                self.gOB[x][y].config(width=8, height=4)

    def butfun(self,args):
        if self.player == self.turn:
            self.add(args)
            if (self.count<=9 and self.won==""):
                self.getcomp()

    def setlis(self, args):
        self.lis = args
        while len(args)!=3 and len(self.gOB):
            print("error")
        try:
            for x in [0,1,2]:
                for y in [0,1,2]:
                    if x>=0 and x<=2 and y>=0 and y<=2:
                        if self.lis[x][y] == "X":
                            self.gOB[x][y].config(text="X",state="disabled")
                        if self.lis[x][y] == "O":
                            self.gOB[x][y].config(text="O",state="disabled")
                        else:
                            pass
        except Exception as e:
            print("error in setlis = ", end=None)
            print(e)
            print(x,y)

    def getcomp(self):
        self.add(self.comp_obj.getval(self.lis))

    def choce(self):
        mb = Mb()
        msgboxthread = Thread(target=mb.run, name="msgthread",args=(self, "X O-games", "What you want to play as", "X", "O"))
        msgboxthread.start()
        msgboxthread.join()
        if self.player == "O":
            self.getcomp()

    def add(self,toadd):
        for x in range(0,3):
            for y in range(0,3):
                if toadd == self.lis[x][y]:
                    self.lis[x][y] = self.turn
                    self.moves.append(toadd)
                    if self.turn == "X":
                        self.turn = "O"
                    else:
                        self.turn = "X"
                    self.setlis(self.lis)
                    self.ck(self.lis)
                    self.comp_obj.getpossiblexo(self.moves)
                    self.count+=1
                    return True
        return False

    def ck(self,ck_lis=[]):
        for i in range(3):
            if (ck_lis[i][0] == ck_lis[i][1] == ck_lis[i][2]):
                self.won=ck_lis[i][0]
            elif (ck_lis[0][i] == ck_lis[1][i] == ck_lis[2][i]):
                self.won=ck_lis[0][i]
        if (ck_lis[0][0] == ck_lis[1][1] == ck_lis[2][2]) or (ck_lis[2][0] == ck_lis[1][1] == ck_lis[0][2]):
            self.won=ck_lis[1][1]
        if self.won == "X":
            self.moves.append("X")
            self.endgame("x won the game")
        elif self.won == "O":
            self.moves.append("O")
            self.endgame("O won the game")
        elif self.count >=9:
            self.moves.append("D")
            self.endgame("Draw")

    def endgame(self,msg=""):
        self.comp_obj.save(self.moves)
        self.player = ""
        mb = Mb()
        msgboxthread = Thread(target=mb.run, name="msgthread",args=(self, "X O-games", msg+"\nDo you want to play again", "Yes", "No"))
        msgboxthread.start()
        msgboxthread.join()
        if self.player=="":
            self.endgame()
        elif self.player == "X":
            self.gui.quit()
        elif self.player == "O":
            self.mobj.end = True
            self.gui.quit()
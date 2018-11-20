from File import *
from random import *


class AI():
    def __init__(self,obj):
        self.main_obj = obj
        self.fr_obj = ReadFile()
        self.memory = []
        self.memory = self.fr_obj.get()
        self.xlis = []
        self.olis = []
        self.dlis = []
        try:
            for e in self.memory:
                if e[len(e) - 1] == "X":
                    self.xlis.append(e)
                elif e[len(e) - 1] == "O":
                    self.olis.append(e)
                elif e[len(e) - 1] == "D":
                    self.dlis.append(e)
                else:
                    print("error getting data")
        except TypeError:
            pass

    def save(self,lis):
        self.fw_obj = WriteFile()
        self.fw_obj.save(lis)

    def getpossiblexo(self,moves=[]):
        self.pxlis = []
        self.pxlis.clear()
        self.polis = []
        self.polis.clear()
        self.pdlis = []
        self.pdlis.clear()
        for x in self.xlis:
            if x[0:len(moves)] == moves:
                self.pxlis.append(x)
        for o in self.olis:
            if o[0:len(moves)] == moves:
                self.polis.append(o)
        for d in self.pdlis:
            if d[0:len(moves)] == moves:
                self.pdlis.append(d)

    def getval(self,xo_lis):
        self.xo_lis = xo_lis
        self.rem_place=[]
        for e in range(3):
            for d in range(3):
                if xo_lis[e][d] == "X" or xo_lis[e][d] == "O":
                    pass
                else:
                    self.rem_place.append(xo_lis[e][d])
        self.nturns = 9 - len(self.rem_place)
        if self.memory is None:
            return self.getran()
        elif self.main_obj.player == "O":
            if len(self.pxlis)>1:
                if self.nturns == 0:
                    return self.xlis[randint(0, len(self.xlis)-1)][0]
                else:
                    return self.pxlis[randint(0, len(self.pxlis)-1)][self.nturns]
            elif len(self.pxlis)==1:
                return self.pxlis[0][self.nturns]
            elif len(self.pdlis)>1:
                return self.pdlis[randint(0, len(self.pdlis)-1)][self.nturns]
            elif len(self.pdlis)==1:
                return self.pdlis[0][self.nturns]
            else:
                return self.getran()

        elif self.main_obj.player == "X":
            if len(self.polis)>1:
                if self.nturns == 1:
                    return self.polis[randint(0, len(self.polis)-1)][1]
                else:
                    return self.polis[randint(0, len(self.polis)-1)][self.nturns]
            elif len(self.polis)==1:
                return self.polis[0][self.nturns]
            elif len(self.pdlis)>1:
                return self.pdlis[randint(0, len(self.pdlis)-1)][self.nturns]
            elif len(self.pdlis)==1:
                return self.pdlis[0][self.nturns]
            else:
                return self.getran()

    def getran(self):
        while True:
            temp = int(str(randint(1,3))+str(randint(1,3)))
            for x in self.rem_place:
                if temp == x:
                    return temp
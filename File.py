from ast import *


class ReadFile:
    def get(self):
        rf = open("winMoves", "r")
        ran = False
        lis = []
        for e in rf:
            lis.append(literal_eval(e))
            ran = True
        if(ran):
            return lis
        else:
            return None


class WriteFile:
    def save(self,lis_to_save):
        sf = open("winMoves", "a")
        sf.write(str(lis_to_save) + "\n")

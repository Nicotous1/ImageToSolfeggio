from __future__ import division
from lib.AdvancedImage import AdvancedImage

class Note:

    def __init__(self, trait, portee):
        self.os = trait
        self.portee = portee
        self.castred = False
        self.searchSize = int(portee.getPureHeight()*0.25) + 1
        self.TR, self.TL, self.BR, self.BL = -1, -1 ,-1 ,-1
        self.whoIAm()


    ## Renvoie true si note en haut
    def amIReverse(self):
        return  self.getTR() > self.getBL()


    def whoIAm(self):
        self.getBR()
        self.getTL()

        if self.castred:
            step = 0.56
        else:
            step = 0.61

        if self.amIReverse():
            y = self.os.getTop()
            if self.getTR() > step:
                if self.getBL() > 0.02 or self.getBR() > 0.02:
                    time = 0.5
                else:
                    time = 1
            else:
                time = 2
        else:
            y = self.os.getBottom()
            if self.getBL() > step:
                if self.getTL() > 0.02 or self.getTR() > 0.02:
                    time = 0.5
                else:
                    time = 1
            else:
                time = 2

        name = self.portee.getNoteNameOfY(y)

        self.deal_with_ids(name)
        self.time = time


    def deal_with_ids(self, ids):
        if type(ids) is int or type(ids) is float:
            self.freq = ids
            self.name = str(ids) + "Hz"
        else:
            self.name = ids
            self.freq = self.freq_with_name(ids)


    def freq_with_name(self,name):
        if name == "Do":
            return 262
        if name == "Re":
            return 294
        if name =="Mi":
            return 330
        if name == "Fa":
            return 349
        if name == "Sol":
            return 392
        if name == "La":
            return 440
        if name == "Si":
            return 494
        if name == "Do2":
            return 523
        if name == "Re2":
            return 554
        if name == "Mi2":
            return 587
        if name == "Fa2":
            return 622
        if name == "Sol2":
            return 659
        if name == "La2":
            return 698.5
        return 440 #DEFAULT LA


    def __str__(self):
        if self.amIReverse():
            s = "reverse"
        else:
            s = "normal"
        phrase = self.name + " (" + str(self.time) + " beat) - " + s + " - (" + str(round(self.getTL(),2)) + ";" + str(round(self.getTR(),2)) + ";" + str(round(self.getBR(),2)) + ";" + str(round(self.getBL(),2)) + ")"

##        phrase = phrase + "\n" + str(self.os)
##
##        X1 = self.os.getRight() + 1
##        X2 = X1 + int(self.searchSize)
##        Y1 = self.os.getTop() - int(self.searchSize*0.5)
##        Y2 = Y1 + self.searchSize
##        phrase = phrase +  "\nTR : " + str(X1) + " ; " + str(X2) + " ; " + str(Y1) + " ; " + str(Y2) + " -> " + str(self.getRatio(X1, X2, Y1, Y2))
##
##        X2 = self.os.getLeft() - 1
##        X1 = X2 - int(0.4*self.searchSize)
##        Y1 = self.os.getTop() - int(self.searchSize*0.7)
##        Y2 = Y1 + self.searchSize
##        phrase = phrase +  "\nTL : " + str(X1) + " ; " + str(X2) + " ; " + str(Y1) + " ; " + str(Y2) + " -> " + str(self.getRatio(X1, X2, Y1, Y2))
##
##
##        X1 = self.os.getRight() + 1
##        X2 = X1 + int(0.8*self.searchSize)
##        Y1 = self.os.getBottom() - int(self.searchSize*0.5)
##        Y2 = Y1 + self.searchSize
##        phrase = phrase +  "\nBR : " + str(X1) + " ; " + str(X2) + " ; " + str(Y1) + " ; " + str(Y2) + " -> " + str(self.getRatio(X1, X2, Y1, Y2))
##
##        X2 = self.os.getLeft() - 1
##        X1 = X2 - int(self.searchSize)
##        Y1 = self.os.getBottom() - int(self.searchSize*0.6)
##        Y2 = Y1 + self.searchSize
##        phrase = phrase +  "\nBL : " + str(X1) + " ; " + str(X2) + " ; " + str(Y1) + " ; " + str(Y2) + " -> " + str(self.getRatio(X1, X2, Y1, Y2))
##
##        phrase = phrase + "\nCastred -> " + str(self.castred)
##
##        phrase = phrase + "\n\n"

        return phrase

    ## Fonction de ratio
    def getTR(self):
        if self.TR == -1:
            X1 = self.os.getRight() + 1
            X2 = X1 + int(self.searchSize)
            Y1 = self.os.getTop() - int(self.searchSize*0.5)
            Y2 = Y1 + self.searchSize
            self.TR = self.getRatio(X1, X2, Y1, Y2)

        return self.TR

    def getTL(self):
        if self.TL == -1:
            X2 = self.os.getLeft() - 1
            X1 = X2 - int(0.4*self.searchSize)
            Y1 = self.os.getTop() - int(self.searchSize*0.7)
            Y2 = Y1 + self.searchSize
            self.TL = self.getRatio(X1, X2, Y1, Y2)
        return self.TL

    def getBR(self):
        if self.BR == -1:
            X1 = self.os.getRight() + 1
            X2 = X1 + int(0.8*self.searchSize)
            Y1 = self.os.getBottom() - int(self.searchSize*0.5)
            Y2 = Y1 + self.searchSize
            self.BR = self.getRatio(X1, X2, Y1, Y2)
        return self.BR

    def getBL(self):
        if self.BL == -1:
            X2 = self.os.getLeft() - 1
            X1 = X2 - int(self.searchSize)
            Y1 = self.os.getBottom() - int(self.searchSize*0.6)
            Y2 = Y1 + self.searchSize
            self.BL = self.getRatio(X1, X2, Y1, Y2)
        return self.BL

    def getRatio(self,X1,X2,Y1,Y2):
        img = AdvancedImage()
        black = 0
        tot = 0
        for y in range(Y1, Y2):
            if y in self.portee.getBlackY():
                self.castred = True
                continue
            for x in range(X1, X2):
                if img.get(x,y) == 1:
                    black = black + 1
                tot += 1
        return black/tot

    def getFreq(self):
        return self.freq

    def getName(self):
        return self.name

    def getTime(self):
        return self.time


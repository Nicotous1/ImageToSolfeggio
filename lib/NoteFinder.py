from __future__ import division
from lib.Line import Line
from lib.Note import Note

class NoteFinder:
    def __init__(self,img):
        self.img = img

    def isNote(self,img,x,lines):
        compteur=0
        max=0
        for y in lines:
            if img.get(x,y)==1:
                compteur+=1
            else:
                if compteur>max:
                    max=compteur
                compteur=0
        if compteur > max:
            max = compteur
        return max >= 3

    def getNoteLinesOfPortee(self,portee):
        img = self.img
        begin=portee.getLeft()
        end=portee.getRight()
        y=self.getInterestingY(portee)
        res=[]
        k=0
        line1=None
        line2=None
        for x in xrange(begin,end):
            if self.isNote(img,x,y):
                line = self.getLineOfX(x,img,portee)
                line1=line
                if line != None:
                    if res!=[] and line1.isMyArm(res[len(res) - 1]):
                        res[len(res) - 1]+=line1
                    else:
                        res.append(line1)
                line2=line1
        return self.purify(res, portee)

    def getNotesOfPortee(self,portee):
        lines=self.getNoteLinesOfPortee(portee)
        notes=[]
        for line in lines :
            notes.append(Note(line, portee))
        return notes

    def purify(self, lines, portee):
        res = []
        for line in lines:
            if portee.isMyBone(line) == False:
              res.append(line)
        return res
                            


    def getLineOfX(self,x,img,portee):
        maxLine=None
        currentLine=None
        for y in range(portee.getTop(),portee.getBottom()+1):

            if img.get(x,y)==1:
                if currentLine==None:
                    currentLine=Line(x,x,y,y)
                else:
                    currentLine.etire()
                if maxLine==None:
                    maxLine=currentLine

            if currentLine!= None and ( img.get(x,y)==0 or y == portee.getBottom()):
                if maxLine == None :
                    maxLine=currentLine
                elif maxLine.getHeight() < currentLine.getHeight():
                    maxLine=currentLine
                currentLine = None
        if maxLine.getHeight() < 0.4*portee.getHeight():
            return None
        return maxLine


    #
    # Retourne les ordonnees
    #
    def getInterestingY(self, portee):
        interestingId = [1,2,4,6,8,10,12,13]
        interestingY = []
        for i in interestingId:
            interestingY.append(portee.getLine(i-1).getMiddle())
        return interestingY














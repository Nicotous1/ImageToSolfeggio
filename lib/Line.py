"""
    Ligne
"""
class Line:
    def __init__(self, x1, x2, y1, y2):
        if x1 > x2: x1,x2 = x2,x1
        self.x1 = int(x1)
        self.x2 = int(x2)
        if y1 > y2: y1,y2 = y2,y1
        self.y1 = int(y1)
        self.y2 = int(y2)

    def isOnMyLine(self,line):
        X = line.getX()
        return not(X[1] < self.x1 and self.x2 < X[0]) #Ligne Strictement sur Les Meme Lignes

    def isMyArm(self,line):
        if line == None :
            return False
        return  self.x2==line.x1-1 or self.x1==line.x2+1



    def isFamily(self, line):
        return (line.getHeight() == self.getHeight() and line.getWidth() == self.getWidth())


    def expend(self):
        self.x2 += 1

    def etire(self):
        self.y2 += 1

    def __add__(self,other):
        return Line(min(self.x1,other.x1), max(self.x2,other.x2), min(self.y1, other.y1), max(self.y2, other.y2))

    def __str__(self):
        return "Line --- X(" + str(self.x1) + "," + str(self.x2) + ") --- Y(" + str(self.y1) + "," + str(self.y2) + ") --- Size(" + str(self.getWidth()) + "," + str(self.getHeight()) + ")"

    def getX(self):
        return (self.x1, self.x2)

    def getY(self):
        return (self.y1, self.y2)

    def getBottom(self):
        return self.y2

    def getTop(self):
        return self.y1

    def getLeft(self):
        return self.x1

    def getRight(self):
        return self.x2

    def getWidth(self):
        return self.x2 - self.x1 + 1

    def getHeight(self):
        return self.y2 - self.y1 + 1

    def copy(self):
        return Line(self.x1,self.x2,self.y1, self.y2)

    def translateY(self, y):
        self.y1 += int(y)
        self.y2 += int(y)
        return self

    def moveUp(self, y):
        self.translateY(-y)
        return self

    def moveDown(self, y):
        self.translateY(y)
        return self

    def setY(self,y1, y2):
        self.y1 = int(y1)
        self.y2 = int(y2)
        return self

    def getMiddle(self):
        return (self.y1 + self.y2) * 0.5

    def isMyBody(self,line):
        return self.getBottom()+1 == line.getTop()
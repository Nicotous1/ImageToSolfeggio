from __future__ import division
from lib.Line import Line
from lib.Note import Note

#
# Une portee contient 13 lignes dont 5 en noir sur l'image
#
class Portee:

    notesLine = list(reversed(("Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do2", "Re2", "Mi2", "Fa2", "Sol2", "La2")))

    def __init__(self, lines):

        self.blackY = None

        # Si il n'y a pas exactement 5 lignes, on retourne une erreur (Stop l'execution)
        if len(lines) != 5: raise NameError("Une portee doit contenir exactement 5 lignes ! (" + str(len(lines)) + " lignes fournies)")

        # On genere toutes les lignes de la portee
        self.generateAllLines(lines)

    def getBlackY(self):
        if self.blackY == None:
            blackLines = [2,4,6,8,10]
            self.blackY = []
            for blackLine in blackLines:
                self.blackY = self.blackY + range(self.getLine(blackLine).getTop(), self.getLine(blackLine).getBottom() + 1)
        return self.blackY


    # Retourne si le y est dans la portee
    def isIn(self, y):
        return (self.getTop() <= y and y <= self.getBottom())

    def getNoteNameOfY(self, y):
        if self.isIn(y) == False:
            return None

        for i in range(len(self.lines)-1):
            line1 = self.lines[i]
            line2 = self.lines[i+1]

            top = line1.getTop()
            bottom = line2.getBottom()
            middleY = (top + bottom)/2

            if top <= y and y <= middleY:
                return Portee.notesLine[i]
            if middleY < y and y <= bottom:
                return Portee.notesLine[i+1]


    # Genere les lignes manquantes (non tracee) avec les lignes noirs de la portee
    def generateAllLines(self, brutLines):

        # Generation des lignes des DO
        ecart= abs(brutLines[0].getBottom() - brutLines[1].getTop())
        topLine = brutLines[0].copy().moveUp(ecart)
        bottomLine = brutLines[len(brutLines) - 1].copy().moveDown(ecart)

        # Ajout des lignes des DO aux blackLines
        blackLines = []
        blackLines.append(topLine)
        blackLines += brutLines
        blackLines.append(bottomLine)

        # Rajout des lignes non tracee en intercalation
        self.lines = [] # Array des lignes finales
        for i in range(len(blackLines)):
            # On ajoute la ligne noire
            self.lines.append(blackLines[i])

            # Si on est pas a la derniere ligne noire
            if i < len(blackLines) - 1:
                # On ajoute la ligne entre cette ligne noire et la prochaine
                self.lines.append(self.getInterLigne(blackLines[i], blackLines[i+1]))


    def getInterLigne(self, ligne1, ligne2):

        # On assure que ligne 1 est au dessus de ligne 2
        if ligne1.getBottom() < ligne2.getTop():
            temp = ligne1.copy()
            ligne1 = ligne2.copy()
            ligne2 = temp

        # Generation de l'interligne
        ligne = ligne1 + ligne2 # On fusionne les deux lignes (histoire d'avoir les x fusionner)
        y = (ligne1.getBottom() + ligne2.getTop())*0.5 # On calcul y de l'interligne
        ligne.setY(y,y) # On modifie la ligne en une ligne de 1 pixel sur y

        return ligne

    def isMyBone(self, line):
        return (self.getLine(2).getTop() == line.getTop() and self.getLine(10).getBottom() == line.getBottom())


    # Renvoie la ligne numero i
    def getLine(self, i):
        return (self.lines[i])

    def getPureHeight(self):
        return abs(self.getLine(2).getTop() - self.getLine(10).getBottom())

    def getHeight(self):
        #return self.getBottom() - self.getTop() + 1
        return int(self.getPureHeight()*2)

    def getTop(self):
        return self.getLine(2).getTop() - int(self.getPureHeight()*0.5)

    def getBottom(self):
        return self.getLine(10).getBottom() + int(self.getPureHeight()*0.5)

    def getRight(self):
        return self.getLine(0).getRight()
    def getLeft(self):
        return self.getLine(0).getLeft()

    def __str__(self):
        r = "Portee :\n"
        for line in self.lines:
            r += str(line) + "\n"
        return r

    def getLines(self):
        return self.lines


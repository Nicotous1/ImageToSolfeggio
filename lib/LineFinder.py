from __future__ import division
from lib.Line import Line
from math import floor

"""
    Line Finder :
        Cherche les lignes de la partition dans une image
"""
class LineFinder:

    min = 0.2 # taille minimale d'une ligne en % de la page

    #
    #   Line getLineOn(AdvancedImage, int)
    #   Retourne la plus grande ligne possible sur une ordonnee y de l'image
    #
    def getLineOn(self, img, y):

        line = None
        maxLine = None
        minWidth = LineFinder.min*img.getWidth()

        for x in range(img.getWidth()):

            if img.get(x,y) == 1:
                if line != None:
                    line.expend()
                else:
                    line = Line(x,x,y,y)
            else:
                if line != None and line.getWidth() >= minWidth and (maxLine == None or maxLine.getWidth() < line.getWidth()):
                    maxLine = line
                line = None

        if line != None and line.getWidth() >= minWidth and (maxLine == None or maxLine.getWidth() < line.getWidth()): return line

        return maxLine

    #
    #   [Line] findLines(AdvancedImage [, int])
    #   Trouve les lignes par tous les moyens
    #
    def findLines(self, img,p = 0.007):
        print "Recherche des lignes..."

        #Initialisation Variables
        lines = [] #Tableau contenant les lignes sures.
        yList = [] #Indice horizontale de tous les matched probable (Histoire de ne pas avoir a les retrouver dans la recherche Hardcore)
        n = int(floor(p*img.getWidth())) #Nombre de ligne de recherche verticale. Soit p % de la largeur de l'image.
        h = img.getWidth()/n #Largeur entre chaque ligne de recherche
        
        #Parcours Verticlale
        for y in range(img.getHeight()):

            matched = 0 #Compte le nombre de points succesif

            for i in range(1,n): #Parcours horizontale selon les lignes de recherches

                 # Test sur le pixel de la ligne de recherche verticale i
                 if img.get(h*i,y) == 1: matched +=1 #Si pixel noir, on incremente matched
                 else: matched = 0 #Sinon on reinitialise matched

                # Test de detection de la ligne
                 if matched >= LineFinder.min*n: #Ligne Probable car le nombre minimum de point sucessif et atteint (la ligne fait LineFinder.min% de la page)
                    yList.append(y) #On ajoute l'ordonne de la ligne aux probables

                    k = len(lines) - 1 #Indice de la ligne precedente ajoutee

                    # Si il y a une ligne precedente et qu'elle est juste au dessus (C'est la meme ligne etaler sur plusieur pixel)
                    if k >= 0 and lines[k].getBottom() + 1 == y:
                        lines[k].etire() #On reprend donc la ligne precedente et on l'etire vers le bas de 1px
                        # Warning : On n'ajoute pas les deux lignes car la precedente et plus precise car elle est extraite de getLineOn

                    # Cette ligne est le debut d'une nouvelle ligne
                    else:
                        # On analyse toute la ligne de l'image pour en extraire la ligne exacte
                        line = self.getLineOn(img,y)
                        if line != None: # Si il y a bien une ligne on l'ajoute aux lignes sures
                            lines.append(line)
                            line = None

                    # On passe a l'autre ligne horizontale
                    break
                 # Si il n'y a aucun matched et que on est deja a plus de (1 - min) alors il n'y a aucune chance de trouver une ligne.
                 if matched == 0 and i > (1-LineFinder.min)*n: #Abandon
                    break # On passe a la suivante

        # Toutes l'images a ete analysee de maniere simple
        # On verifie la validite des lignes trouvees (si toute ligne appartient a une portee)
        if len(lines) % 5 != 0:
            # Une ligne n'a pas de portee.
            print "Echec recherche simple (" + str(len(lines)) + " lignes detectee) !"
            # On lance la recherche approfondi
            lines = self.harcoreFinder(yList,img)

        # On verifie encore le resultat
        if len(lines) % 5 != 0: raise NameError("La detection des lignes a echouee ! Certaines lignes n'on pas de portee ! (" + str(len(lines)) + " lignes detectee)") # Cela a encore echouee s'en est fini ! On lance une erreur !

        # Tous c'est bien passe on retourne les lignes
        print str(len(lines)) + " lignes trouvees."
        return lines

    #
    #   [Line] harcoreFinder([int] , AdvancedImage)
    #   Retourne les lignes des portees sur l'image de maniere la plus hardcore possible !
    #   Si on doit en arriver la que dieu nous vienne en aide pour trouver les notes !!
    #
    def harcoreFinder(self,listY, img):
        print "Recherche Hardcore..."
        lines = []

        # On parcours les y probables trouver precedement
        for y in listY:
            line = self.getLineOn(img,y) #On recupere ici pour CHAQUE ligne probable. La meilleur ligne possible de cette y. (On parcours donc a chaque fois toute la ligne...)

            # Meme algorythme de fusion
            if line != None:
                k = len(lines) - 1
                if k >= 0:
                    if lines[k].getBottom() + 1 == line.getBottom(): #Ligne Colle -> Fusion
                        lines[k] = lines[k] + line
                    else:
                        lines.append(line)
                else: lines.append(line)
            line = None

        return lines



from lib.LineFinder import LineFinder
from lib.AdvancedImage import AdvancedImage
from lib.Portee import Portee
from lib.NoteFinder import NoteFinder

class Partition:

    def __init__(self,link = None):
        self.hasCalculed = False
        self.img = None
        self.link = None
        if link != None:
            self.link = link
            self.img = AdvancedImage(link)
        self.portees = None
        self.notes = []

    def getPortees(self):
        if self.img == None:
            return []
        if self.portees == None:
            #Recuperation des lignes
            LF = LineFinder()
            lines = LF.findLines(self.img)

            #Creation des portees
            self.portees = []
            i = 1
            packet = []
            for line in lines:
                packet.append(line)
                if len(packet) == 5:
                    self.portees.append(Portee(packet))
                    packet = []

        return self.portees

    def __str__(self):
        if (self.link == None):
            r = "Partition Custom\n"
        else:
            r = "--- Partition '" + str(self.link) + "' ---\n"
            r += str(len(self.getPortees())) + " portees et " + str(len(self.getNotes())) + " notes.\n"
        if len(self.getNotes()) > 0:
            r += "Notes :\n"
            for note in self.getNotes():
                r += "  __ " + str(note) + "\n"
        else:
            r += "Aucune Note\n"
        r += "\n"
        return r


    def getImg(self):
        return self.img

    def setNotes(self, notes):
        self.notes = notes
        return self

    def getNotes(self):
        if self.hasCalculed == False:
            finder = NoteFinder(self.getImg())
            for portee in self.getPortees():
                for note in finder.getNotesOfPortee(portee):
                    self.notes.append(note)

        return self.notes

    def append(self, note):
        self.notes.append(note)
        return self
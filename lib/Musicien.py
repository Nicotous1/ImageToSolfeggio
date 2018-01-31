from __future__ import division
from winsound import Beep

class Musicien:

    def play(self, partition, tempo = 120):
        print "Lecture de la partition (" + str(tempo) +"bpm)"
        a=[]
        notes = partition.getNotes()
        i = 0
        print "Playing " + str(len(notes)) + " notes..."
        for note in notes:
            i = i + 1
            print str(note) + " || " +  str(int(i/len(notes)* 100)) + "%"
            self.playNote(note, tempo)



    # Fct elementaire pour jouer une seule note
    def playNote(self, note, tempo):
        time = self.getRealTimeFor(note,tempo) #en s
        Beep(int(note.getFreq()),int(time * 1000))

    # Retourne le temps en seconde d'une note en fct du tempo
    def getRealTimeFor(self, note,tempo):
        return note.getTime()*60/tempo

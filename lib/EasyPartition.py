from lib.Note import Note
from lib.Partition import Partition

# Permet de generer une partition avec differentes types de donnees simple
class EasyPartition:

    # Genere avec un array du tuple :
    # [(nom,time),...]
     def generate(self, notes):
         partition = Partition()
         for note in notes:
             partition.append(Note(note[0], note[1]))
         return partition
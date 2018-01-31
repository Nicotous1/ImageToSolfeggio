from lib.Timer import Timer
from lib.Partition import Partition
from lib.Musicien import Musicien
###################################
timer = Timer(True)
#MAIN EXECUTION

partition = Partition("img/partition_4.jpg") # Retourne une partition
mozart = Musicien()
mozart.play(partition)


#Rapport
print str(round(partition.getImg().getEfficacity(), 2)) + "%"

#END MAIN EXECUTION
print " --------"
timer.stop()
###################################

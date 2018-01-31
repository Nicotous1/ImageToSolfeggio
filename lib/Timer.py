from __future__ import division
import time

class Timer:

    def __init__(self, start = False):
        self.result = None
        self.start = None
        if start: self.start = time.time()

    def averageTime(self, f, p, n=20):
        timeTot = 0
        print "Calculating..."
        for i in range(n):
            start_time = time.time()
            f(p)
            timeTot += time.time() - start_time
            print str(int(i/20.0*100)) + "%"
        print "--- " + str(int(timeTot/n * 1000)) + "ms ---"

    def start(self):
        self.start = time.time()

    def stop(self, show = True):
        if self.start != None:
            self.result = time.time() - self.start
            self.start = None
        if show:
            if self.result != None: print str(self.result*1000) + " ms"
            else : print "Aucune mesure !"
        elif self.result != None:
            if show: print str(self.result*1000) + " ms"


# racquetball.py

from random import random
import math

def main(A, B, repeats):

    winsA = 0
    winsB = 0

    for n in range(repeats):
        #single game
        #set both scores to zero
        scoreA = 0
        scoreB = 0

        #set the initial server to be player A
        service = "A"

        while scoreA < 15 and scoreB < 15:

            if service == "A":
                if random() < A:
                    scoreA = scoreA+1
                else:
                    service = "B"
            else:
                if random() < B:
                    scoreB = scoreB + 1
                else:
                    service = "A"

        if scoreA == 15:
            winsA = winsA + 1
        else:
            winsB = winsB + 1


    print "Games simulated: ", repeats
    print "Wins for A: ", winsA, "(", float(winsA)/repeats*100, ")"
    print "Wins for B: ", winsB, "(", float(winsB)/repeats*100, ")"

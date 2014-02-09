#monks.py

"""Move n discs from post A to post C with 3 rules:\\
1. move one disc at a time
2. never move a larger disc on top of a smaller disc
3. never set a disc aside"""

def mDisc(n, source, dest, temp):
	#if n is 1 the move is just A to C
	if n == 1:
		print "Move disc from ", source, " to ", dest, "."
	else:
		mDisc(n-1, source, temp, dest)
		mDisc(1, source, dest, temp)
		mDisc(n-1, temp, dest, source)

def monk(n):
	mDisc(n,'A','C','B')
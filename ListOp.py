#ListOp.py

"""Recreate list operations"""

def count(myList,x):
	"""returns the number of times x appears in the list"""

	counter = 0						# initialize counter
	
	for i in myList:

		if i == x:
			counter += 1

	return counter


def isin(myList, x):
	"""returns true if x is found in myList, otherwise returns false"""
	
	for i in myList:

		if i == x:
			return True

	return False


def index(myList, x):
	"""returns the index of the first occurance of x"""
	
	for i in range(len(myList)):
		if myList[i] == x:
			return i

	print x, " is not in list"



def reverse(myList):
	"""Reverses the list"""
	RevList = []
	for i in myList:
		RevList.insert(0,i)

	return RevList


def merge(l1,l2,l3):		#l1 and l2 are lists to be merged into l3 in order
	i1, i2, i3 = 0,0,0			#initialize a counter for all 3 lists

	while i1 < len(l1) and i2 < len(l2):

		if l1[i1] > l2[i2]:
			l3[i3] = l2[i2]
			i2 += 1
			i3 += 1
		else:
			l3[i3] = l1[i1]
			i1 += 1
			i3 += 1

	while i1 < len(l1):
		l3[i3] = l1[i1]
		i1 += 1
		i3 += 1
	while i2 < len(l2):
		l3[i3] = l2[i2]
		i2 += 1
		i3 += 1 


def mySort(myList):
	"""Returns sorted list"""	
	if len(myList) > 1:
		mid = len(myList)/2
		
		list1 = myList[:mid]
		list2 = myList[mid:]

		mySort(list1)
		mySort(list2)

		merge(list1, list2, myList)

	return myList





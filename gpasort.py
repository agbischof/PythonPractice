#gpasort.py

"""A program to sort student information into GPA order"""
import string
from grades import Student, makeStudent, readStudents, writeStudents

def cmpGPA(s1,s2):
	#function that compares two students based on GPA
	return cmp(s1.getGPA(),s2.getGPA())

def cmpCredits(s1,s2):
	#function that compares two students based on Credits
	return cmp(s1.getHours(), s2.getHours())

def cmpName(s1,s2):
	#function that orders students by name 
	return cmp(s1.getName(), s2.getName())

def main(fileIn, fileOut, sortBy, ForB):
	data = readStudents(fileIn)
	if sortBy.lower() == 'gpa':
		data.sort(cmpGPA)
	elif sortBy.lower() == 'credits':
		data.sort(cmpCredits)
	elif sortBy.lower() == 'name':
		data.sort(cmpName)
	else:
		print "sortBy not defined appropriately"

	if ForB.lower() == 'b':
		data.reverse()
		
	writeStudents(data, fileOut)

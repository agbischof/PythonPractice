#grades.py

import string
import math

class Student:
	def __init__(self, name, hours, qpoints):
		self.name = name
		self.hours = float(hours)
		self.qpoints = float(qpoints)

	def getName(self):
		return self.name

	def getHours(self):
		return self.hours

	def getQPoints(self):
		return self.qpoints

	def getGPA(self):
		return self.qpoints/self.hours

def makeStudent(infoStr):
	#input file: tab-separated line with student name, hours, and qpoints
	#returns Student object
	name, hours, qpoint = string.split(infoStr, "\t")
	return Student(name, hours, qpoint)


def main(file):
	stu = open(file)
	best = makeStudent(stu.readline())
	
	for line in stu:
		s = makeStudent(line)
		new_better = s.getGPA() > best.getGPA()
		if new_better:
			best = s
	print 'final best: ', best.getName(), best.getGPA() 

	stu.close()


def readStudents(file):

	#reads all the students in file and puts them in a list

	stu = open(file, 'r')

	students = []
	for line in stu:
		students.append(makeStudent(line))
	stu.close()
	return students

def writeStudents(students, filename):
	outfile = open(filename, 'w')
	for s in students:
		outfile.write("%s\t%f\t%f\n" %(s.getName(), s.getHours(), s.getQPoints()))

	outfile.close()





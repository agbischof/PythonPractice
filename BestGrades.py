import string
import math

def main(file):

	stu = open(file)

	BestGPA = 0

	for line in stu:
		data = string.split(line)
		GPA = float(data[3])/float(data[2])

		print data[1], data[0], GPA, " of ", data[3], " credits."
		if GPA > BestGPA:
			BestGPA = GPA
			BestStu = data

	print BestStu [1], BestStu[0], BestGPA, " of ", BestStu[3], " credits!" 
# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
	print "This program illustrates a chaotic function"
	x1, x2 = input('Enter 2 numbers between 0 and 1 separated by commas: ')
#	x2 = input('Enter another number between 0 and 1: ')
	
	print "input     ", x1, "      ", x2
	for i in range(10):
		x1 = 3.9*x1*(1-x1)
		x2 = 3.9*x2*(1-x2)
		print "          ", x1, "      ", x2

if __name__ == "main":
	main()


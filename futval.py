#file: futval.py
#A program to calculate the interest on a user input capital 

def main():

	print "This program calculates the final principle after a given number of years"
	principal, apr, years = input("Input the initial investment, the annual percentage rate expressed in decimal, and the number of years projected out, separated by commas: ")

	for i in range(years):
		principal = principal*(1+apr)

	print
	print
	print "The value in", years, "years is: ", principal

if __name__ == "main":
	main()
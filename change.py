#change.py
#A program to calculate the value of some change in dollars

def main():
    print "Change Counter"
    print
    print "Please enter the count of each coin type."
    quarters = input("Quarters: ")
    dimes = input("dimes: ")
    nickels = input("nickels: ")
    pennies = input("pennies: ")
    total = quarters*.25+dimes*.1+nickels*.05+pennies*.01
    print
    print "The total value of your change is", total

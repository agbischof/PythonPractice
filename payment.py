#payment.py
#This program computes weekly pay
#inputs: hours worked, and hourly wage
#assumptions: overtime (over 40 hours) assumed to be time and a half
#output: total pay for 1 week of work

import math #makes math library available

def main(hours, wage):

    

    if hours < 40:
        pay = hours*wage

    else:
        pay = 40*wage + (hours-40)*wage*1.5

    print pay

    
if __name__ == 'main()':
    main()

#Palindrome.py
"""Tests a string to see if it is palindrome, ignoring spaces punctuation and capitilization"""

import string
import re

def TestPal(s1, pal):

	if len(s1) > 1 and pal:			#as long as the length of the string is greater then 1 test
		
		if s1[0] == s1[-1]:			#if the 1st letter equals the last letter continue
			
			newStr = s1[1:-1]		
			
			pal = TestPal(newStr, pal)	#pass all but 1st and last letter on to test again
			
		else:						#if 1st letter doesn't equal last it is not a palindrome, set to false and stop
			pal = False
			
	return pal


def main(s1):

	s1 = s1.lower()									#convert string to lowercase

	p = re.compile("[!'#$%&()*+,-./:;<=>?@[\\]^_{|}~\" ]+")
	s1 = re.sub(p,'',s1)

	outcome = TestPal(s1, True)
	
	if outcome:
		print "A palindrome!!!"
	else:
		print "Not a palindrome.."

if __name__ == '__main__':
	import sys
	s1 = sys.argv[1]
	main(s1)


"""
Even Pairs
Question :
Have the function EvenPairs(str) take the str parameter being passed and determine if a
pair of adjacent even numbers exists anywhere in the string. If a pair exists, return the
string true, otherwise return false. For example: if str is "f178svg3k19k46" then there
are two even numbers at the end of the string, "46" so your program should return the
string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12)
so your program should return the string true.

Examples
Input: "3gy41d216"
Output: true

Input: "f09r27i8e67"
Output: false
"""

import re

def EvenPairs(input_string):

	temp1 = re.findall(r'\d+', input_string) #use regex to extract numbers from string
	num_list = list(map(int, temp1)) 


	for num in num_list:

		num_digits = len(str(num))
		if num_digits>=2:
			digits = list(str(num))			

			for i in range(1,num_digits):
				first_half = int(str(num)[0:i])
				second_half = int(str(num)[i:num_digits])

				if first_half%2==0 and second_half%2==0:
					return True


	return False



if __name__=="__main__":

	print(EvenPairs("f178svg3k19k46")) #True
	print(EvenPairs("7r5gg812")) #True
	print(EvenPairs("3gy41d216")) #True
	print(EvenPairs("f09r27i8e67")) #False

#Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

import string

def ispangram(str1, alphabet = string.ascii_lowercase):

	#Create a set of the alphabet
	alphabet = set(alphabet)
	print(alphabet)
	#Remove spaces from the input string
	str1 = str1.replace(' ','')
	print (str1)
	#Convert the input string to all lowercase
	str1 = str1.lower()
	print (str1)
	#Grab all unique letters from the string
	str1 = set(str1)
	print (str1)
	#Compare alphanet set to string set
	return str1 == alphabet

print (ispangram("The quick brown fox jumps over the lazy dog"))

Will be staying with our daughter and family. And we are planning to visit various tourist placed in Ontario and also help my daughter during her post partum.
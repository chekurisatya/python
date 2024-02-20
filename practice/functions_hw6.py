#Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
	return s == s[::-1]

print (palindrome('helleh'))
print (palindrome('malayalam'))
print (palindrome('hello'))
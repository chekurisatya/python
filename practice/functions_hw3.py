#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.


def up_low(s):
	upCount = 0
	lowCount = 0
	for ch in s:
		if ch.isupper() and ch.isalpha():
			upCount += 1
		elif ch.islower() and ch.isalpha():
			lowCount += 1
		else:
			pass
	return (upCount, lowCount)
text = 'Hello Mr. Rogers, how are you this fine Tuesday?'
text1 = "12342413@@(*$@($@*#)@*!@$(!@#)@!#!@)"

upC,lowC = up_low(text)

print (upC,lowC)

upC,lowC = up_low(text1)

print (upC,lowC)
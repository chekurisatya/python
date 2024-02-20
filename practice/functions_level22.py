#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(word):
	result = ""
	for ch in word:
		result += ch*3
	return result

print (paper_doll('Hello'))
print (paper_doll('Mississippi'))

#MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
	words = sentence.split()
	words.reverse()
	return " ".join(words)

print (master_yoda("I am home"))
print (master_yoda("We are Home"))

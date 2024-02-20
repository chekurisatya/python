#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
	words = text.split()
	return words[0][0] == words[1][0]

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
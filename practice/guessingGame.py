#Guessing Game:
#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

#If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#On a player's first turn, if their guess is
#within 10 of the number, return "WARM!"
#further than 10 away from the number, return "COLD!"
#On all subsequent turns, if a guess is
#closer to the number than the previous guess return "WARMER!"
#farther from the number than the previous guess, return "COLDER!"
#When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

import random

num = random.randint(0,101)
print (f'{num}')
guessCount = 0
guesses = [0]
gNum = int(input("Guess a number:"))
while True:
	#Check if the guessed number is out of bounds
	if gNum < 1 or gNum > 100:
		print (f'WHOA!!! {gNum} OUT OF BOUNDS. Guess a number between 1 and 100 included')
	
	#If the player guesses the number correctly then end the game.
	if gNum == num:
		print ("CONGRATULATIONS!!! YOUR GUESS IS CORRECT")
		print (f'It took you {len(guesses)} Guesses')
		break
	#Append the guess to the list.
	guesses.append(gNum)

	# The if condition shall be false for the first incorrect guess only. For all subsequent guesses, the if section will get executed.
	if guesses[-2]:
		if abs(gNum - num) < abs(gNum-guesses[-2]):
			print ("WARMER!")
		else:
			print ("COLDER!")
	else:
		if abs(gNum - num) <= 10 :
			print ("WARM!")
		else:
			print ("COLD!")

	gNum = int(input("Guess Again:"))

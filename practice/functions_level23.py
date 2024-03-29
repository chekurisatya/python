#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
	if a+b+c <=21:
		return a+b+c
	elif (a+b+c > 21) and 11 in (a,b,c):
		if (a + b + c) - 10 <= 21:
			return (a + b + c) - 10
		else:
			return 'BUST'
	else:
		return 'BUST'

print (blackjack(5,6,7)) # --> 18
print (blackjack(9,9,9)) # --> 'BUST'
print (blackjack(9,9,11)) # --> 19
print (blackjack(11,11,11))
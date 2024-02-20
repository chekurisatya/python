#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers #are odd

def min_even(a,b):
	if a % 2 == 0 and b % 2 == 0:
		return min(a,b)
	else:
		return max(a,b)

print (min_even(2,4))
print (min_even(2,5))
print (min_even(10,555))
print (min_even(5,7))
print(min_even(8,10))
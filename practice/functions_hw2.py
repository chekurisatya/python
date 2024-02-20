#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
	if num >= low and num <= high:
		return f'{num} is in range between {low} and {high}'
	else:
		return f'{num} is not in range between {low} and {high}'

def ran_bool(num,low,high):
	return num >= low and num <= high

print (ran_check(5,2,7))
print (ran_check(10,1,9))

print (ran_bool(5,2,7))
print (ran_bool(10,1,9))

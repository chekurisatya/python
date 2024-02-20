#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
	return a + b == 20 or a == 20 or b == 20

print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(12,9))
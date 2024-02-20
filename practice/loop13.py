#Exercise 13: Find the factorial of a given number
n = 5
res = 1
print(n,'factorial is ',end=' ')
while n > 0:
	res = res * n
	n -= 1
print(res)

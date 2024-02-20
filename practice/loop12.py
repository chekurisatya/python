#Exercise 12: Display Fibonacci series up to 10 terms
first = 0 
next1 = 1
for i in range(10):
	print (first, end=' ')
	fib_term = first + next1
	first = next1
	next1 = fib_term

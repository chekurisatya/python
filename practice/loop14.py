#Exercise 14: Reverse a given integer number
n = 12345
rev_num = 0
while n > 0:
	rem = n % 10
	rev_num = (rev_num * 10) + rem
	n = n // 10
print(f'The reverse number is : {rev_num}')
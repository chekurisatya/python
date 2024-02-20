#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(list1):
	res = ''
	count_0 = 0

	for n in list1:
		while count_0 < 2:
			if n == 0:
				res += str(n)
				count_0 += 1
			else:
				break
		while count_0 == 2:
			if n == 7:
				res += str(n)
				count_0 += 1
				break
			else:
				break
	if res == '007':
		return True
	else:
		return False

def spy_game1(list2):
	code = [0,0,7,'x']

	for num in list2:
		if num == code[0]:
			code.pop(0)
	if len(code) == 1:
		return True
	else:
		return False


print (spy_game1([1,2,4,0,0,7,5]))
print (spy_game1([1,0,2,4,0,5,7]))
print (spy_game1([1,7,2,0,4,5,0]))
print (spy_game1([7,0,0]))
print (spy_game1([0,0,0]))
print (spy_game1([0,0,7]))

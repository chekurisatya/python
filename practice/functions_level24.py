#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be 
#followed by at least one 9). Return 0 for no numbers.

def summer_69(nums):
	if len(nums) == 0:
		return 0
	total = 0
	add = True
	for n in nums:
		while add:
			if n != 6:
				total += n
				break
			else:
				add = False
		while not add:
			if n != 9:
				break
			else:
				add = True
				break
	return total

print (summer_69([1, 3, 5])) #should print 9
print (summer_69([4, 5, 6, 7, 8, 9, 6, 7, 10, 9, 1, 1, 1, 9, 6, 9, 0, 7])) #should print 28
print (summer_69([2, 1, 6, 9, 11])) #should print 14
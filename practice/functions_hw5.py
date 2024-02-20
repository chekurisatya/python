 #Write a Python function to multiply all the numbers in a list.

def multiply(nums):
	prod = 1
	for n in nums:
		prod *= n
	return prod

sample_list = [1,4,10,8,9,56]

print (multiply(sample_list))
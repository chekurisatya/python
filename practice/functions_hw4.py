#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(list1):
	return set(list1)

Sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]

unique_items = unique_list(Sample_list)

print (f'The Unique Items in the list are {unique_items}')

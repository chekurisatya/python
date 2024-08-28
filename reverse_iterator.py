#Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::

class reverse_iter:

	def __init__(self, lst):
		self.lst = iter(reversed(lst))

	def __iter__(self):
		return self

	def __next__(self):
		try:
			return next(self.lst)
		except StopIteration:
			raise StopIteration
		

it = reverse_iter([1,2,3,4,5,6,7])

for item in it:
	print(item)

'''
Write a function count_elements that takes a list of integers and returns a dictionary with the count of each element using Counter.
'''

from collections import Counter

def count_elements(lst):
    c = Counter(lst)
    return dict(c)
# Test
print(count_elements([1, 2, 2, 3, 3, 3]))
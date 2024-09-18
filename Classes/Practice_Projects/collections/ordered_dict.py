'''
Using OrderedDict to Maintain Order
Write a function sort_dict_by_value that takes a dictionary and returns an OrderedDict where the items are sorted by their values.

'''
from collections import OrderedDict

def sort_dict_by_value(d):
    # Implement this function using OrderedDict
    return sorted(d.items(), key = lambda x: x[1])

# Test
print(sort_dict_by_value({'apple': 3, 'banana': 1, 'orange': 2}))
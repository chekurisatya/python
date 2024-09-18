'''
Using ChainMap to Merge Dictionaries
Write a function merge_dictionaries that takes two dictionaries and merges them into a single view using ChainMap.
'''
from collections import ChainMap

def merge_dictionaries(d1, d2):
    # Implement this function using ChainMap
    d = ChainMap(d1,d2)
    return dict(d)

# Test
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2))
'''
2. Finding Most Common Elements with Counter
Write a function most_common_elements that takes a list of strings and returns the 3 most common elements using Counter.
'''
from collections import Counter

def most_common_elements(lst):
    c = Counter(lst).most_common(2)
    return c

# Test
print(most_common_elements(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))

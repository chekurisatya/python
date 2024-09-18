'''
8. Using defaultdict for Counting
Write a function count_characters that takes a string and counts the occurrence of each character using defaultdict.
'''
from collections import defaultdict

def count_characters(s):
    d = defaultdict(int)
    for ch in s:
        d[ch] += 1
    return dict(d)
    return sorted(d.items(), key = lambda x : x[1])
# Test
print(count_characters('hello world'))
print(count_characters('malayalam'))
print(count_characters('Lester B. Pearson Toronto International Airport'))
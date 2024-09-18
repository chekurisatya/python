'''
 Using Counter for Word Frequency
Write a function word_frequency that takes a string and returns the frequency of each word using Counter.
'''
from collections import Counter

def word_frequency(s):
    # Implement this function using Counter
    c = Counter(s.split())
    return dict(c)

# Test
print(word_frequency("this is a test this is only a test"))
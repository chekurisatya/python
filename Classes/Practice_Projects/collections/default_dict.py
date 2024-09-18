'''
Using defaultdict for Grouping
Write a function group_words_by_length that takes a list of words and groups them into a dictionary
where the key is the word length, and the value is a list of words of that length. Use defaultdict to implement this.
'''

from collections import defaultdict

def group_words_by_length(words):
    # Implement this function using defaultdict
    d = defaultdict(list)
    for word in words:
        d[len(word)].append(word)
    return dict(d)

# Test
print(group_words_by_length(['apple', 'bat', 'car', 'dog', 'banana']))
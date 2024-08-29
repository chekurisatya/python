#Dictionary comprehension practice
'''
23. Create a dictionary of strings by replacing vowels with underscores

Sample Output
'''
fruits = ['apple', 'banana', 'cherry']

#{'apple': '_ppl_', 'banana': 'b_n_n_', 'cherry': 'ch_rry'}

under_fruits = {k:"".join(["_" if ch in "aeiou" else ch for ch in k]) for k in fruits}

#under_fruits = {k:"".join(["_" for ch in k if ch in "aeiou" else ch]) for k in fruits}
print(under_fruits)

'''
24. Create a dictionary of words and their lengths, but only for words starting with 'a'

Sample Output
'''
fruits = ['apple', 'banana', 'cherry', 'date']

#{'apple': 5}

a_fruits = {k:len(k) for k in fruits if k[0] == 'a'}
print(a_fruits)

'''
25. Create a dictionary of strings by repeating each word thrice

Sample Output
'''
fruits_3 = {k:k*3 for k in fruits}
print(fruits_3)

'''
26. Create a dictionary of strings with words containing 'a' and their lengths

Sample Output
'''
a_lengths = {k:len(k) for k in fruits if 'a' in k}
print(a_lengths)

'''
27. Create a dictionary of numbers and their squares, but only for numbers greater than 5

Sample Output
'''
nums = [1,2,3,4,5,6,7,8,9,10]
square_5 = {k:k**2 for k in nums if k > 5}
print(square_5)

'''
28. Create a dictionary of characters and their ASCII values from a string, excluding non-alphabetic characters

Sample Output

Hello123
'''
var = "Hello123"
ascii_char = {k:ord(k) for k in set(var) if k.isalpha()}
print(ascii_char)

'''
29. Create a dictionary of words and their uppercase forms, excluding words with no uppercase letters

Sample Output

{'Banana': 'BANANA', 'Date': 'DATE'}
'''
fruits = ['apple', 'Banana', 'cherry', 'Date']
upper_fruits = {fruit: fruit.upper() for fruit in fruits if any(char.isupper() for char in fruit)}
print(upper_fruits)

'''
30. Create a dictionary of strings with words containing more than 4 letters

Sample Output
'''
words = "Python is a powerful and versatile programming language"
strings = {word: len(word) for word in words.split(" ") if len(word) > 4}
print(strings)

'''
33. Create a dictionary of numbers with their signs reversed
Sample Output
{5: -5, -10: 10, 15: -15, -20: 20, 25: -25}
'''
nums = [5, -10, 15, -20, 25]
print({k: -k for k in nums})

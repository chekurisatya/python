nums = [1,2,3,4,5,6,7,8,9,10]
print([x**2 for x in nums])

#list of even numbers from 1 to 20
print([x for x in range(21) if x%2 == 0])

#Print a list of charecters from a string
string = "Hello World!"
print([x for x in string])

#4. Create a list of lengths of words in a sentence
string = "This is a sample sentence."
print([len(x) for x in string.split()])

#5. Generate a list of tuples containing a number and its square
nums = [1,2,3,4,5]
print([(x,x**2) for x in nums])

#6. Create a list of lowercase letters
print([chr(x) for x in range(ord('a'), ord('z')+1)])

#7. Generate a list of uppercase letters
print([chr(x).upper() for x in range(ord('a'), ord('z')+1)])

#8. Create a list of even numbers squared and odd numbers cubed from 1 to 10
print([x**2 if x%2==0 else x**3 for x in range(1,11)])

#9. Generate a list of common multiples of 3 and 5 up to 100
print([x for x in range(1,101) if (x%3==0 and x%5==0)])

#10 10. Create a list of reversed strings from another list
words = ['apple','banana','cherry']
print([word[::-1] for word in words])

#17. Generate a list of strings with vowels removed
words = ['apple','banana','cherry']
print(["".join([char for char in word if char not in 'aeiou']) for word in words])

#19. Generate a list of numbers with their signs reversed
nums = [-2, 3, -5, 7, -11]
print([-x for x in nums])

#28. Generate a list of tuples containing two numbers whose sum is even
print([(x,y) for x in range(1,11) for y in range(1,11) if (x+y)%2==0])


#939. Create a list of strings with vowels replaced by asterisks
words = ['apple','banana','cherry']
print(["".join(["*" if char in 'aeiou' else char for char in word]) for word in words])

#43. Create a list of words with their characters sorted
print(["".join(sorted(word)) for word in words])

#45. Create a list of lowercase vowels from a string
string = "Hello World!"
print([char.lower() for char in string if char in 'aeiou'])

#55. Removing whitespace from strings in a list
words = [' hello ', ' world ', ' python ']
print([word.strip() for word in words])

#56. Create a list of characters that are not vowels from a string
print([x for x in string if x not in 'aeiou'])
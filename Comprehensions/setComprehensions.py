#1. Generate a set of squares of numbers from 1 to 10
print({num**2 for num in range(1,11)})

#3. Generate a set of characters from a string
string = "Hello, world!"
print({char for char in set(string) if char.isalpha()})


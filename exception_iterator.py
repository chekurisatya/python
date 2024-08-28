'''
#my_list = [10, 20, 30, 0, "invalid", 50]
my_words = ['Hello','Python','Monty',56,59.0,'Data','Camp','Ford',78,0.78]
my_iterator = iter(my_words)

while True:
    try:
        # Get the next item from the iterator
        result = ''
        item = next(my_iterator)
        if type(item) != str:
            raise TypeError
        # Simulate some processing (e.g., division)
        #result = 100 / item
        result += item
        print(f"{result}")

    except StopIteration:
        # StopIteration is raised when the iterator is exhausted
        print("End of the iterator reached.")
        break  # Exit the loop
    
    except ZeroDivisionError as zde:
        # Handle division by zero
        print(f"Error: Division by zero encountered: {zde}")
    
    except TypeError as te:
        # Handle invalid data type (e.g., non-numeric value)
        print(f"Error: Invalid data type encountered: {te}")
    
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"Unexpected error: {e}")
'''

my_dict = {'a': 1, 'b': 2, 'c': 3}
key_iterator = iter(my_dict)  # Iterator for keys

while True:
    try:
        # Get the next key from the iterator
        key = next(key_iterator)
        print(f"Key: {key}")
    
    except StopIteration:
        # StopIteration is raised when the iterator is exhausted
        print("End of the dictionary keys reached.")
        break  # Exit the loop

my_dict = {'a': 1, 'b': 2, 'c': 3}
value_iterator = iter(my_dict.values())  # Iterator for values

while True:
    try:
        # Get the next value from the iterator
        value = next(value_iterator)
        print(f"Value: {value}")
    
    except StopIteration:
        # StopIteration is raised when the iterator is exhausted
        print("End of the dictionary values reached.")
        break  # Exit the loop


my_dict = {'a': 1, 'b': 2, 'c': 3}
item_iterator = iter(my_dict.items())  # Iterator for key-value pairs

while True:
    try:
        # Get the next key-value pair from the iterator
        key, value = next(item_iterator)
        print(f"Key: {key}, Value: {value}")
    
    except StopIteration:
        # StopIteration is raised when the iterator is exhausted
        print("End of the dictionary items reached.")
        break  # Exit the loop


def number_generator(numbers):
    """
    A generator that yields numbers from a list and handles exceptions.
    
    Args:
        numbers (list): A list of numbers (int/float) to yield.

    Yields:
        int or float: The next number from the list.
    """
    for number in numbers:
        try:
            # Simulate a potential operation that might raise an exception
            result = 100 / number  # This will raise ZeroDivisionError if number is 0
            yield result
        except ZeroDivisionError:
            print(f"Error: Cannot divide by zero (number: {number}).")
        except TypeError:
            print(f"Error: Invalid data type encountered (number: {number}).")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Example usage of the generator with exception handling
numbers = [10, 20, 0, "invalid", 50]

gen = number_generator(numbers)

print(next(gen))
print(next(gen))
print(next(gen))

'''
for value in gen:
    print(f"Yielded value: {value}")
'''
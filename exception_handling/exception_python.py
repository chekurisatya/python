def divide(a,b):
    '''
    This function shall divide 2 numbers.
    The result of the division is returned.
    Input: 2 non-negative whole numbers
    Return: 1 non-negative whole number
    Warnings: Error shall be thrown for Zero Division Errors
    '''
    try:
        res = a/b
    except ZeroDivisionError as E:
        print("An Error Occured:", E)
        return None
    except TypeError as TE:
        print("An Error Occured", TE)
        return None

    return res


s = 'Hello'
#help(divide)
#print(divide(10,0))
print(divide(20,5))
#print(divide(10,s))
#print(divide.__doc__)
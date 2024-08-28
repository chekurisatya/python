#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.WARNING)
def dbz_error(dividend, divisor):
    """
    Divides 2 numbers and returns the result.

    Args:
        dividend (int) : The numerator
        divisor (int)  : The denominator

    Returns:
        int : The result of the division

    Errors:
        A division by zero error shall be thrown if division by integer 0 is attempted.
    """
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError as e:
        logger.error(f'An Error has been encountered: {e}')
        return None



print(dbz_error.__doc__)
print(help(dbz_error))
logger.warning(dbz_error(10,20))
logger.warning(dbz_error(40,0))
logger.warning(dbz_error(40,10))
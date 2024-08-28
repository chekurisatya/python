#7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
'''
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.WARNING)
def keyboard_interrupt():
    try:
        result = input("Enter something")
        return result
    except KeyboardInterrupt as e:
        logger.error(f'An Error has been encountered: {e}')
        return None

keyboard_interrupt()
'''
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.WARNING)


def keyboard_interrupt():
    """Handles KeyboardInterrupt gracefully and logs the error.

    Returns:
        str: The user input if successful, otherwise None.
    """

    try:
        result = input("Enter something: ")
        logger.info(f"User input: {result}")  # Informative logging
        return result
    except KeyboardInterrupt:
        logger.error(f"KeyboardInterrupt")  # Clear error message with context
        return None

if __name__ == "__main__":
    keyboard_interrupt()
    print(keyboard_interrupt.__doc__)
##myapp.py

import logging
import mylib

logger = logging.getLogger(__name__)

def main():
	logging.basicConfig(filename='myapp.log', level = 10)
	logger.debug("In Debug Mode")
	logger.info("Started logging")
	mylib.doSomething()
	logger.info("Finished Logging")

if __name__ == '__main__':
	main()
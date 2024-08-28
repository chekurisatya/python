import logging

logger = logging.getLogger('THISFILE')
logging.basicConfig(
	format = '%(asctime)s:%(levelname)s:%(message)s', 
	filename = 'example.log', 
	filemode = 'w', 
	encoding = 'utf-8', 
	level = logging.DEBUG
	)

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

'''
logger = logging.getLogger("THISFILE")
logging.basicConfig(filename = 'example.log', filemode = 'w',format='%(levelname)s:%(message)s', level = logging.DEBUG)
logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')


logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s')
logging.warning("This should print the time now.")
'''
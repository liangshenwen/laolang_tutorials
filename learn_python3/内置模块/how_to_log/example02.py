import logging

logging.basicConfig(filename='example02.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
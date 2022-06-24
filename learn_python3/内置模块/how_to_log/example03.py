import logging

logging.basicConfig(filename='example03.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
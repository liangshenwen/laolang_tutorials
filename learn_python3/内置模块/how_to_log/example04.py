import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


name_1 = 'John'
name_2 = 'Samo'

logging.error('%s raised an error', name_1)
# using f-string
logging.error(f'{name_2} raised an error')
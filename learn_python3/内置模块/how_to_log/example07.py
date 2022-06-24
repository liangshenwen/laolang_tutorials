import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# a custom logger can’t be configured using basicConfig(). You have to configure it using Handlers and Formatters.
# logger = logging.getLogger('example_logger')
# It is recommended that we use module-level loggers by passing __name__ as the name parameter to getLogger() to
# create a logger object as the name of the logger itself would tell us from where the events are being logged
logger = logging.getLogger(__name__)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

import example06
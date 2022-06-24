import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(process)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


a = 5
b = 0

try:
    c = a / b
except ZeroDivisionError as e:
    logging.error("Exception occurred: %s", e,  exc_info=True)
    logging.info('no exec info')
    logging.error("Exception occurred", exc_info=False)
    # it is equal to logging.error("Exception occurred: %s", e,  exc_info=True)
    logging.exception("Exception occurred: %s", e)

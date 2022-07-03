from china_stats_data.spiders import PopulationSpider, PopulationRatioSpider

import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

logger = logging.getLogger(__name__)


def run_by_single_thread():
    logger.info('spider app starts.')
    spiders = [
        PopulationSpider(),
        PopulationRatioSpider()
    ]

    for spider in spiders:
        spider.run()

    logger.info('spider app complete.')


def run_by_multiple_thread():
    logger.info('spider app starts.')
    pool = ThreadPoolExecutor(max_workers=5)
    spiders = [
        PopulationSpider(),
        PopulationRatioSpider()
    ]

    future_tasks = [pool.submit(spider.run()) for spider in spiders]

    for task in as_completed(future_tasks):
        try:
            logger.info(task.result)
        except Exception as e:
            logger.error('error happened.', exc_info=1)
        else:
            logger.info('task is done')

    pool.shutdown()

    logger.info('spider app complete.')


def run_by_multiple_process():
    logger.info('spider app starts.')
    pool = ProcessPoolExecutor(max_workers=5)
    spiders = [
        PopulationSpider(),
        PopulationRatioSpider()
    ]

    future_tasks = [pool.submit(spider.run()) for spider in spiders]

    for task in as_completed(future_tasks):
        try:
            logger.info(task.result)
        except Exception as e:
            logger.error('error happened.', exc_info=1)
        else:
            logger.info('task is done')

    pool.shutdown()

    logger.info('spider app complete.')


if __name__ == '__main__':
    run_by_multiple_thread()
    # run_by_multiple_process()
    # run_by_single_thread()

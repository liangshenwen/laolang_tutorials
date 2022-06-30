import traceback

from china_stats_data.spiders.base_spider import BaseSpider


class PopulationSpider(BaseSpider):
    def __init__(self):
        super().__init__(level_1='treeZhiBiao_4_a', level_2='treeZhiBiao_30_a')


if __name__ == '__main__':
    spider = PopulationSpider()
    try:
        spider.start()
        spider.make_ui_data_ready()
        data_df = spider.extract_ui_data()
        print(data_df)
    except Exception as e:
        traceback.print_exc()
    finally:
        spider.stop()

import traceback

from china_stats_data.spiders.base_spider import BaseSpider


class PopulationRatioSpider(BaseSpider):
    """从国家统计局网站抓取人口出生率、死亡率和自然增长率.
    """
    def __init__(self):
        # level_1(人口)->level_2(人口出生率、死亡率和自然增长率)
        super().__init__(level_1='treeZhiBiao_4_a', level_2='treeZhiBiao_31_a')


if __name__ == '__main__':
    spider = PopulationRatioSpider()
    try:
        spider.start()
        spider.make_ui_data_ready()
        data_df = spider.extract_ui_data()
        print(data_df)
    except Exception as e:
        traceback.print_exc()
    finally:
        spider.stop()





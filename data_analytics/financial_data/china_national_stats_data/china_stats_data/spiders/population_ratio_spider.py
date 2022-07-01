import time

from sqlalchemy.types import Integer, Float

from china_stats_data.spiders.base_spider import BaseSpider


class PopulationRatioSpider(BaseSpider):
    """从国家统计局网站抓取`人口出生率、死亡率和自然增长率`相关数据.
    """
    def __init__(self):
        """初始化相关参数
        level_1(人口)->level_2(人口出生率、死亡率和自然增长率)
        """
        super().__init__(level_1='treeZhiBiao_4_a',
                         level_2='treeZhiBiao_31_a',
                         table_name='population_ratio',
                         table_col_types={
                             '年份': Integer(),
                             '人口出生率(‰)': Float(),
                             '人口死亡率(‰)': Float(),
                             '人口自然增长率(‰)': Float()
                         })


if __name__ == '__main__':
    spider = PopulationRatioSpider()
    spider.run()
    time.sleep(100)





import time

from sqlalchemy.types import Integer

from china_stats_data.spiders.base_spider import BaseSpider


class PopulationSpider(BaseSpider):
    """从国家统计局网站抓取`总人口`相关数据.
    """
    def __init__(self):
        """初始化相关参数
        level_1(人口)->level_2(总人口)
        """
        super().__init__(level_1='treeZhiBiao_4_a',
                         level_2='treeZhiBiao_30_a',
                         table_name='population',
                         table_col_types={
                             '年份': Integer(),
                             '年末总人口(万人)': Integer(),
                             '男性人口(万人)': Integer(),
                             '女性人口(万人)': Integer(),
                             '城镇人口(万人)': Integer(),
                             '乡村人口(万人)': Integer()
                         })


if __name__ == '__main__':
    spider = PopulationSpider()
    spider.run()
    time.sleep(100)

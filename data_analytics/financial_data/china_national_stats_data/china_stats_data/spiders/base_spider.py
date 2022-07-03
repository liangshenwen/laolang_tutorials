import re
import traceback
import logging

from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By

from china_stats_data.config import DATA_QUERY_URL
from china_stats_data.utils import database_utils
from china_stats_data.utils.selenium_utils import get_chrome_driver, wait_for_element

logger = logging.getLogger(__name__)


class SpiderException(Exception):
    pass


class BaseSpider:
    def __init__(self,
                 level_1: str,
                 level_2: str,
                 table_name: str,
                 table_col_types: dict,
                 url: str = DATA_QUERY_URL,
                 year_input: str = 'last40'):
        self.url = url
        self.level_1 = level_1
        self.level_2 = level_2
        self.year_input = year_input
        self.table_name = table_name
        self.table_col_types = table_col_types

    def _start(self):
        # 获取chrome浏览器驱动
        self.driver = get_chrome_driver()
        self.driver.get(self.url)

    def _make_ui_data_ready(self):
        # 点击‘人口’导航栏
        population_ele = wait_for_element(self.driver, By.ID, self.level_1)
        population_ele.click()

        # 点击‘人口出生率、死亡率和自然增长率’导航栏
        total_population_ele = wait_for_element(self.driver, By.ID, self.level_2)
        total_population_ele.click()

        # 点击‘时间’ 下拉框
        time_select_ele = wait_for_element(self.driver, By.CSS_SELECTOR, '#mySelect_sj > div.dtHtml > div.dtHead')
        time_select_ele.click()

        # 选择‘最近40年’的数据
        time_input_ele = wait_for_element(self.driver,
                                          By.CSS_SELECTOR,
                                          '#mySelect_sj > div.dtHtml > div.dtBody > div.dtFoot > input')
        time_input_ele.send_keys(self.year_input)
        ok_button_ele = wait_for_element(self.driver,
                                         By.CSS_SELECTOR,
                                         '#mySelect_sj > div.dtHtml > div.dtBody > div.dtFoot > div.dtTextBtn')
        ok_button_ele.click()

    def _extract_ui_data(self) -> pd.DataFrame:
        html = self.driver.page_source
        soup = BeautifulSoup(markup=html, features='html.parser')

        data_table = soup.find(lambda tag: tag.name.lower() == 'table' and
                                           tag.has_attr('class') and
                                           tag['class'] == ['public_table', 'table_fix'])

        data_dict = {'年份': []}
        for tr_idx, tr in enumerate(data_table.tbody.children):
            td_lst = list(tr.children)
            col_name = ''
            for th_idx, th in enumerate(data_table.thead.tr.children):
                # 判断是否指标列
                if th.text == '指标':
                    col_name = td_lst[th_idx].text
                    data_dict[col_name] = []

                # 判断是否年份数据列
                else:
                    year_match = re.match(r'(\d{4})年', th.text)
                    if year_match:
                        year = year_match.group(1)
                        if year not in data_dict['年份']:
                            data_dict['年份'].append(year)
                        col_value = td_lst[th_idx].text
                        if col_name != '':
                            data_dict[col_name].append(col_value)

        return pd.DataFrame(data=data_dict)

    def _stop(self):
        if self.driver:
            self.driver.quit()

    def run(self) -> str:
        try:
            logger.info('start to run spider: %s', __name__)
            self._start()
            self._make_ui_data_ready()
            data_df = self._extract_ui_data()
            db_engine = database_utils.get_db_engine()
            effected_rows = data_df.to_sql(name=self.table_name, con=db_engine, if_exists='replace', index=False,
                                           dtype=self.table_col_types)
            logger.info('%d records are updated into table:%s', effected_rows, self.table_name)
            return 'Success'
        except Exception as e:
            logger.error('error happened when run spider:%s', __name__, exc_info=1)
            return 'Failure'
        finally:
            self._stop()
            logger.info('end spider: %s', __name__)

import os

# 等待元素出现的超时时间，单位为秒
ELE_WAIT_TIMEOUT: float = 10
# 等待元素出现的轮询间隔时间，单位为秒
ELE_WAIT_POOL_FREQ: float = 0.5
# 页面加载的超时时间，单位为秒
PAGE_WAIT_TIMEOUT: float = 60
# 数据查询URL
DATA_QUERY_URL = 'https://data.stats.gov.cn/easyquery.htm?cn=C01'
# 配置的根路径
CONFIG_ROOT_PATH = r'C:\Users\sliang\development\github\laolang_tutorials\data_analytics\financial_data\china_national_stats_data'


def get_driver_path():
    return os.path.abspath(CONFIG_ROOT_PATH + '/selenium/chromedriver.exe')


def get_db_path():
    return os.path.abspath(CONFIG_ROOT_PATH + '/sqlite/china_stats_data.db')

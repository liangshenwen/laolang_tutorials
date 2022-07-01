from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from china_stats_data.config import ELE_WAIT_TIMEOUT, ELE_WAIT_POOL_FREQ, PAGE_WAIT_TIMEOUT
from china_stats_data.config import get_driver_path


def get_chrome_driver() -> webdriver:
    options = webdriver.ChromeOptions()
    # 忽略证书无效的错误
    options.add_argument('ignore-certificate-errors')
    driver_path = get_driver_path()
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(PAGE_WAIT_TIMEOUT)
    return driver


def wait_for_element(driver: webdriver,
                     by: str,
                     value: str,
                     timeout: float = ELE_WAIT_TIMEOUT,
                     poll_frequency: float = ELE_WAIT_POOL_FREQ):
    ele = WebDriverWait(driver, timeout, poll_frequency).until(ec.presence_of_element_located((by, value)))
    return ele

from selenium import webdriver
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class WebUIInit:
    # 初始化
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def get_elements(self, xpath):
        el = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))  # 元素可见时返回元素对象 自动等待元素出现 参数是元组，所以要多加一组小括号
        logger.info(f"元素定位成功：tag_name{el.tag_name}")
        return el

    def goto(self, url):
        self.driver.get(url)

    def input(self, param1, param2):
        element = self.get_elements(param1)
        element.clear()
        element.send_keys(param2)

    def hide_div(self, param1, param2):
        self.get_elements(param1).click()
        option = self.get_elements(param2)
        self.driver.execute_script("arguments[0].click();", option)

    # 依据不同的定位方法，进行点击操作
    def click(self, param1):
        self.get_elements(param1).click()

    # 定义强制等待
    def sleep(self, seconds):
        time.sleep(seconds)

    # 定义隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def quit(self):
        self.driver.quit()

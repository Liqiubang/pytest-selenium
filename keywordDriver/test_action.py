import time
import logging
logger = logging.getLogger(__name__)
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestAction:
    def __init__(self, driver):
        self.driver = driver

    def get_elements(self, xpath):
        try:
            self.wait = WebDriverWait(self.driver, 10)
            el = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            logger.info(f"元素定位成功：{el.tag_name} (XPath: {xpath})")
            return el
        except TimeoutException:
            logger.error(f"元素定位超时：XPath {xpath}")
            raise

    def goto(self, url):
        self.driver.get(url)

    def asserts(self, param1):
        element = self.get_elements(param1)
        return element.text

    def input(self, param1, param2):
        element = self.get_elements(param1)
        element.clear()
        element.send_keys(param2)

    def get_hide_elements(self, param1, param2):
        self.get_elements(param1).click()
        option = self.get_elements(param2)
        self.driver.execute_script("arguments[0].click();", option)

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

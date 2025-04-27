# conftest.py（核心配置文件）
import pytest
from selenium import webdriver
from typing import Generator
import logging
logger = logging.getLogger(__name__)
from selenium.webdriver.support.wait import WebDriverWait

from keywordDriver.test_webInit import WebUIInit

@pytest.fixture(scope="session")
def browser():
    """全局浏览器管理fixture"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 10)  # 使用driver作为浏览器驱动，并设置最大等待时间
    web_ui = WebUIInit(driver)
    logger.info("夹具初始化完成，浏览器启动成功")
    yield web_ui
    driver.quit()

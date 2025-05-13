# conftest.py（核心配置文件）
import openpyxl
import pytest
from selenium import webdriver
import logging
logger = logging.getLogger(__name__)
from selenium.webdriver.support.wait import WebDriverWait
from keywordDriver.test_action import TestAction

@pytest.fixture(autouse=False, scope="session")
def fixture_browser():
    """全局浏览器管理fixture"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.wait = WebDriverWait(driver, 10)  # 使用driver作为浏览器驱动，并设置最大等待时间
    test_action_object = TestAction(driver)
    logger.info("夹具初始化完成，浏览器启动成功")
    yield test_action_object
    driver.quit()

@pytest.fixture(autouse=False, scope="session")
def fixture_load_excel():
    # 加载excel
    workbook = openpyxl.load_workbook('test_excel.xlsx')
    return workbook.active
@pytest.fixture(scope="session")
def test_case_login(fixture_browser, fixture_load_excel):
    for row in fixture_load_excel.iter_rows(min_row=2, values_only=True):
        # 读取测试用例信息
        case_id = int(row[0])
        step = row[1]
        stepName = row[2]
        action = row[3]
        param1 = row[4]
        param2 = row[5]
        if case_id == 1:
            logger.info(f"step= {step} ,stepName= {stepName}")
            print(f"step= {step} ,stepName= {stepName}")
            # 根据关键字执行相应的操作
            if action == 'name':
                print(f"正在执行第 {case_id}个用例: {param1}")
            elif action == 'goto':
                fixture_browser.goto(param1)
            elif action == 'input':
                fixture_browser.input(param1, param2)
            elif action == 'click':
                fixture_browser.click(param1)
            elif action == 'get_hide_elements':
                fixture_browser.get_hide_elements(param1, param2)
        else:
            continue
    print("\n")
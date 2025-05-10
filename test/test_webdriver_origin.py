import time
import pytest
from webdriver_helper import get_webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def test_login_succ():
    driver = get_webdriver('chrome')  # 启动浏览器
    driver.maximize_window()
    driver.get("http://robindev.cm253.com/#/login")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys(
        "15274438093")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(
        "qewxpa01")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/input').send_keys(
        "2222")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[5]/div/button/span').click()
    # 前置部分，在测试用例之前执行
    yield driver

    # 后置部分，在测试用例之后执行
    print("测试结束")
    driver.quit()

def test_ticket_review(test_login_succ):
    # print(test_login_ok.window_handles)
    # print(test_login_ok.current_window_handle)
    # test_login_ok.switch_to.window(test_login_ok.window_handles[-1])

    time.sleep(6)
    test_login_succ.find_element(By.XPATH, "//span[text()='发票管理']").click()
    time.sleep(1)
    test_login_succ.find_element(By.XPATH, "//span[text()='发票审核']").click()
    time.sleep(1)
    # 待审核
    test_login_succ.find_element(By.XPATH,
                               "/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div").click()
    time.sleep(1)
    # 电子普票
    test_login_succ.find_element(By.XPATH,
                               "/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[2]/div/div/div[7]/div").click()
    time.sleep(1)
    test_login_succ.find_element(By.XPATH, "//span[text()='搜索']").click()
    time.sleep(1)
    # 审核
    test_login_succ.find_element(By.XPATH,
                               "/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[29]/div/button/span").click()
    time.sleep(1)
    # 通过
    test_login_succ.find_element(By.XPATH,
                               "//span[text()='通过']").click()
    time.sleep(3)
    msg = test_login_succ.find_element(By.XPATH, "//p[@class='el-message__content']")
    print("提示语：" + msg.text)
    assert msg.text == "操作成功"
    time.sleep(3)

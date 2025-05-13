import random
from webdriver_helper import get_webdriver
from POM.test_basePage import *
import pytest


@pytest.fixture(scope="session")
def user_driver():
    # 已登录的浏览器
    driver = get_webdriver()
    logger.info("浏览器已启动")
    driver.maximize_window()
    driver.get("http://robindev.cm253.com/#/login")
    page = TestLoginPage(driver)
    page.login("15274438093", "qewxpa01", "3333")
    logger.info("登录成功")
    yield driver  # 生成器的写法 返回driver并暂停，直到yield结束，再执行yield后面的代码
    driver.quit()


@pytest.mark.pom
def test_ticket_ok(user_driver):
    logger.info("发票审核开始测试")
    page = TestTicketPage(user_driver)
    page.ticket_audit()
    assert page.msg_audit.text == "操作成功"
    user_driver.get_screenshot_as_file("a.png")
    logger.info("-------------测试结束---------------")


@pytest.mark.pom
@pytest.mark.parametrize("invoiceSubject,taxIdNo,address,phone,msg,flag", [
    ("测试主体" + str(random.randint(100, 100000)), "111", "长沙", "1", "添加成功", 1),
    ("测试主体" + str(random.randint(100, 100000)), "222", "成都", "2", "添加成功", 2),
    ("测试主体" + str(random.randint(100, 100000)), "333", "重庆", "3", "添加成功", 3)
])
def test_new_ticket(user_driver, invoiceSubject, taxIdNo, address, phone, msg, flag):
    logger.info("新增发票开始测试")
    page = TestNewTicketPage(user_driver)
    page.ticket_add(invoiceSubject, taxIdNo, address, phone)
    assert page.msg.text == msg
    user_driver.get_screenshot_as_png()
    logger.info("-------------测试结束---------------")

    #刷新页面没用
    if flag==1:
        page = TestNewTicketPage(user_driver)
        page.ticket_add(invoiceSubject, taxIdNo, address, phone)
        assert page.msg.text == msg
        user_driver.get_screenshot_as_png()
        logger.info("-------------测试结束---------------")
    else:
        page = TestNewTicketPage(user_driver)
        page.ticket_add2(invoiceSubject, taxIdNo, address, phone)
        assert page.msg.text == msg
        user_driver.get_screenshot_as_png()
        logger.info("-------------测试结束---------------")


if __name__ == "__main__":
    test_new_ticket()

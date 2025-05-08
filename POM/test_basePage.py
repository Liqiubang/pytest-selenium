import logging
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)pip show selenium
class TestBasePage:
    # _loc_msg = "//div[contains(@class, 'ant-message-error') and contains(@class, 'ant-message-custom-content')]/span[2]" #该主体已存在，请重新操作!
    _loc_msg = "//div[contains(@class, 'ant-message-success') and contains(@class, 'ant-message-custom-content')]/span[2]"
    _loc_msg_audit = "//p[@class='el-message__content']"
    # 初始化方法，每次创建对象时调用，第一个参数必须是 self，self指向实例本身
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # 使用driver作为浏览器驱动，并设置最大等待时间
        logger.info("PO 实例化成功")

    def get_element(self, xpath):
        logger.info(f"正在定位元素：{xpath=}")
        allure.attach(self.driver.get_screenshot_as_png(), name="定位截图",
                      attachment_type=allure.attachment_type.PNG)  # 定位前截图
        el = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))  # 元素可见时返回元素对象 自动等待元素出现 参数是元组，所以要多加一组小括号
        logger.info(f"元素定位成功：tag_name{el.tag_name}")
        return el

    def __getattr__(self, item):  # 访问不存在的属性时触发  item=username
        if not item.startswith('_loc_'):  # 避免递归调用
            key = f"_loc_{item}"  # 动态生成属性名 key=_loc_username
            xpath = getattr(self, key)  # 获取_loc_username的属性值  与__getattr__作用不一样
            # pdb.set_trace()
            if xpath is not None:
                return self.get_element(xpath)
        raise AttributeError(f"属性 '{item}' 不存在")

    # def alert_ok(self):
    #     logger.info("正在处理弹窗")
    #     alert = self.wait.until(alert_is_present)
    #     alert.accept()
    #     logger.info("弹窗处理完成")

class TestLoginPage(TestBasePage):
    _loc_username = '/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/input'
    _loc_password = '/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input'
    _loc_vertify = '/html/body/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/input'
    _loc_btn = '/html/body/div/div/div/div[2]/div[1]/form/div[5]/div/button/span'

    def login(self, username, password, vertify):
        logger.info("准备登录")
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.vertify.send_keys(vertify)
        self.btn.click()
        logger.info("登录完成")
        allure.attach(self.driver.get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)  # 交互后截图

class TestTicketPage(TestBasePage):
    _loc_ticket_manage = "//span[text()='发票管理']"
    _loc_ticket_audits = "//span[text()='发票审核']"
    _loc_ticket_no_audit = "/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div"
    _loc_ticket_e_ticket = "/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[2]/div/div/div[7]/div"
    _loc_ticket_search = "//span[text()='搜索']"
    _loc_audit = "/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[29]/div/button/span"
    _loc_passBtn = "//span[text()='通过']"

    def ticket_audit(self):
        # self.alert_ok()
        logger.info("正在处理发票审核")
        self.ticket_manage.click()
        self.ticket_audits.click()
        self.ticket_no_audit.click()
        self.ticket_e_ticket.click()
        self.ticket_search.click()
        self.audit.click()
        self.passBtn.click()
        time.sleep(1)
        self.ticket_manage.click()
        logger.info("发票审核处理完成")
        allure.attach(self.driver.get_screenshot_as_png(), "审核截图", allure.attachment_type.PNG)  # 交互后截图

class TestNewTicketPage(TestBasePage):
    _loc_ticket_manage = "//span[text()='发票管理']"
    _loc_ticket_body = "//span[text()='发票主体']"
    _loc_ticket_new = "/html/body/div/div/main/div/div/div/div/div/div/form/div/div[4]/div/div[4]/button/span"
    _loc_invoiceSubject = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[1]/div/div/div[2]/div/div/input"
    _loc_taxIdNo = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[2]/div/div/div[2]/div/div/input"

    _loc_invoiceScene = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[3]/div/div/div[2]/div/div/div"
    _loc_china_invoice = "//div[@class='ant-select-item-option-content' and text()='国内发票']"

    _loc_invoiceType = "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div/div[4]/div/div/div[2]/div/div/div/div/div"
    _loc_normal_invoice = "//div[@class='ant-select-item-option-content' and text()='增值税普通发票']"

    _loc_address = "//*[@id='address']"
    _loc_phone = "//*[@id='phone']"
    _loc_confirm = "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]/span"

    def ticket_add(self, invoiceSubject, taxIdNo, address, phone):
        logger.info("正在处理发票主体")
        self.ticket_manage.click()
        self.ticket_body.click()
        self.ticket_new.click()
        self.invoiceSubject.send_keys(invoiceSubject)
        self.taxIdNo.send_keys(taxIdNo)

        # # 实例化鼠标
        # action = ActionChains(self.driver)
        # # 鼠标悬停
        # action.move_to_element(self.invoiceScene)
        # # 鼠标执行
        # action.perform()
        # print("-------------------鼠标悬停成功-------------------")

        # print("元素是否可见：", element.is_displayed())
        # print("元素是否可用：", element.is_enabled())
        # print("元素是否被选中：", element.is_selected())

        self.invoiceScene.click()
        option = self.driver.find_element(By.XPATH, self._loc_china_invoice)
        self.driver.execute_script("arguments[0].click();", option)

        self.invoiceType.click()
        option2 = self.driver.find_element(By.XPATH, self._loc_normal_invoice)
        self.driver.execute_script("arguments[0].click();", option2)

        self.address.send_keys(address)
        self.phone.send_keys(phone)
        self.confirm.click()
        logger.info("发票主体处理完成")
        allure.attach(self.driver.get_screenshot_as_png(), "发票主体截图", allure.attachment_type.PNG)  # 交互后截图

    def ticket_add2(self, invoiceSubject, taxIdNo, address, phone):
        logger.info("正在处理发票主体")
        self.ticket_new.click()
        self.invoiceSubject.send_keys(invoiceSubject)
        self.taxIdNo.send_keys(taxIdNo)

        self.invoiceScene.click()
        option = self.driver.find_element(By.XPATH, self._loc_china_invoice)
        self.driver.execute_script("arguments[0].click();", option)

        self.invoiceType.click()
        option2 = self.driver.find_element(By.XPATH, self._loc_normal_invoice)
        self.driver.execute_script("arguments[0].click();", option2)

        self.address.send_keys(address)
        self.phone.send_keys(phone)
        self.confirm.click()
        logger.info("发票主体处理完成")
        allure.attach(self.driver.get_screenshot_as_png(), "发票主体截图", allure.attachment_type.PNG)  # 交互后截图



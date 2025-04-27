import openpyxl
import pytest
import logging
logger = logging.getLogger(__name__)
class TestCase1:
    @pytest.fixture(autouse=True, scope="session")
    def test_case_login(self, browser,test_data):
        for row in test_data.iter_rows(min_row=2, values_only=True):
            # 读取测试用例信息
            case_id = int(row[0])
            step = row[1]
            stepName = row[2]
            action = row[3]
            param1 = row[4]
            param2 = row[5]
            if case_id == 1:
                logger.info(f"step= {step} ,stepName= {stepName}")
                print(f"\n step= {step} ,stepName= {stepName}")
                # 根据关键字执行相应的操作
                if action == 'name':
                    print(f"Test Case {case_id}: {param1}")
                elif action == 'goto':
                    browser.goto(param1)
                elif action == 'input':
                    browser.input(param1, param2)
                elif action == 'click':
                    browser.click(param1)
                elif action == 'hide_div':
                    browser.hide_div(param1, param2)
            else:
                continue
        browser.driver.get_screenshot_as_file("case_login.png")
        browser.sleep(5)

    def test_case_ticket(self, browser,test_data):
        for row in test_data.iter_rows(min_row=9, values_only=True):
            # 读取测试用例信息
            case_id = int(row[0])
            step = row[1]
            stepName = row[2]
            action = row[3]
            param1 = row[4]
            param2 = row[5]
            if case_id == 2:
                logger.info(f"step= {step} ,stepName= {stepName}")
                print(f"step= {step} ,stepName= {stepName}")
                if action == 'name':
                    print(f"Test Case {case_id}: {param1}")
                elif action == 'goto':
                    browser.goto(param1)
                elif action == 'input':
                    browser.input(param1, param2)
                elif action == 'click':
                    browser.click(param1)
                elif action == 'hide_div':
                    browser.hide_div(param1, param2)
            else:
                continue
        browser.driver.get_screenshot_as_file("case_ticket.png")
        browser.sleep(5)
        # 运行测试用例
    if __name__ == "__main__":
        test_case_ticket()
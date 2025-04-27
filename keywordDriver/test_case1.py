import pytest
import logging

logger = logging.getLogger(__name__)


class TestCase1:
    @pytest.fixture(scope="session")
    def test_case_login(self, fixture_browser, fixture_load_excel):
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

    # 第minRow开始，执行第caseId个用例，
    @pytest.mark.parametrize("minRow,caseId", [(9, 2)])
    def test_cases(self, test_case_login, fixture_browser, fixture_load_excel, minRow, caseId):
        for row in fixture_load_excel.iter_rows(min_row=minRow, values_only=True):
            # 读取测试用例信息
            case_id = int(row[0])
            step = row[1]
            stepName = row[2]
            action = row[3]
            param1 = row[4]
            param2 = row[5]
            if case_id == caseId:
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
        fixture_browser.driver.get_screenshot_as_file("case_login.png")
        fixture_browser.sleep(5)

    if __name__ == "__main__":
        test_cases()

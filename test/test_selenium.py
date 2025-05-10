import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.add_argument("--disable-gpu")  # 禁用GPU加速‌
# options.add_argument("--disable-extensions")  # 关闭扩展插件
# options.add_argument("--no-sandbox")  # 绕过沙盒限制‌
# options.add_argument("--headless")  # 无头模式减少渲染耗时‌
# driver = webdriver.Chrome(options=options)
def test_tickets_review():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://robindev.cm253.com/#/login")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys(
        "15274438093")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(
        "qewxpa01")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/input').send_keys(
        "1111")
    driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[5]/div/button/span').click()
    time.sleep(6)

    driver.find_element(By.XPATH, "//span[text()='发票管理']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='发票审核']").click()
    time.sleep(1)
    # 待审核
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[1]/div/div/div[2]/div").click()
    time.sleep(1)
    # 电子普票
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/main/div/div/div[2]/div[2]/form/div[2]/div/div/div[7]/div").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='搜索']").click()
    time.sleep(1)
    # 审核
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div/main/div/div/div[2]/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[29]/div/button/span").click()
    time.sleep(1)
    # 通过
    driver.find_element(By.XPATH,
                        "//span[text()='通过']").click()
    time.sleep(3)
    msg = driver.find_element(By.XPATH, "//p[@class='el-message__content']")
    print("提示语：" + msg.text)
    assert msg.text == "操作成功"
    time.sleep(3)
    driver.quit()

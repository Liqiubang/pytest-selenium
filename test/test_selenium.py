# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # options = webdriver.ChromeOptions()
# # options.add_argument("--disable-gpu")  # 禁用GPU加速‌
# # options.add_argument("--disable-extensions")  # 关闭扩展插件
# # options.add_argument("--no-sandbox")  # 绕过沙盒限制‌
# # options.add_argument("--headless")  # 无头模式减少渲染耗时‌
# # driver = webdriver.Chrome(options=options)
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://robindev.cm253.com/#/login")
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys(
#     "15274438093")
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(
#     "qewxpa01")
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/input').send_keys(
#     "1234")
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/form/div[5]/div/button/span').click()
# time.sleep(3)
# driver.quit()

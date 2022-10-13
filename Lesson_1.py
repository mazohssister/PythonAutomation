from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\sonya\PycharmProjects\PythonAutomation\chromedriver.exe')
driver.get('https://www.saucedemo.com/')  #открываем браузер по ссылке
driver.maximize_window()  #раскрывает браузер полностью

user_name = driver.find_element(By.XPATH, "//input[@value='user-name']")  #better to use this command
user_name.send_keys("standard_user")
password = driver.find_element(By.XPATH, "//input[@value='password']")
password.send_keys("secret_sauce")
button_login = driver.find_element(By.XPATH, "//input[@value='login-button']")
button_login.click()

# time.sleep(3)  #задаем время задержки перед закрытием браузера
# driver.close()  #полностью закрываем браузер


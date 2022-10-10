import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\sonya\PycharmProjects\PythonAutomation\chromedriver.exe')
driver.get('https://www.saucedemo.com/')  #открываем браузер по ссылке
driver.maximize_window()  #раскрывает браузер полностью
time.sleep(3)  #задаем время задержки перед закрытием браузера
driver.close()  #полностью закрываем браузер


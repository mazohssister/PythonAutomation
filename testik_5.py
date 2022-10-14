"""Import some libs"""
import datetime
import time
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

""""Make some configurations"""
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s = Service(r'C:\Users\sonya\PycharmProjects\PythonAutomation\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_userxx"
password_for_all = "secret_sauce"

"""Make an input in Login & Password"""

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
user_name.send_keys(Keys.BACKSPACE*2)

password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(password_for_all)
password.submit()  # also you can use var.send_keys(Keys.RETURN OR enter) to imitate enter
print("Input password")

'''Make a scroll down'''
# time.sleep(0.5)
# driver.execute_script("window.scrollTo(0, 500)")  # we can scroll in each side of page, x- horizontal axis, y- vertical
#100 px is one scroll of the mouse wheel

'''Move to lower element without scroll'''
action = ActionChains(driver)
red_tshirt = driver.find_element(By.XPATH, "//footer[@class='footer']")
action.move_to_element(red_tshirt).perform()

# now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d")
# name_screenshot = 'screen ' + now_date + '.png'
# driver.save_screenshot(name_screenshot)














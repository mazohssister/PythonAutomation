"""Import some libs"""
import time
import datetime
from PIL import Image
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

""""Make some configurations"""
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # add option to selenium not to close browser after test ends
driver = webdriver.Chrome(options=chrome_options)

s = Service(r'C:\Users\sonya\PycharmProjects\PythonAutomation\chromedriver.exe')
driver = webdriver.Chrome(service=s)
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
password.submit() # also you can use var.send_keys(Keys.RETURN OR enter) to imitate enter
print("Input password")

'''Click and choose the second line of Filter'''
filter_list = driver.find_element(By.XPATH, "//select[@data-test='product_sort_container']")
filter_list.click()
print("Click Filter")
time.sleep(2)
filter_list.send_keys(Keys.ARROW_DOWN, Keys.ENTER)

'''Make a screenshot of the result'''
# driver.save_screenshot('Result.png')
# screen1 = Image.open('Result.png')
# screen1.show()

# ss = Screenshot_clipping.Screenshot()
# screen_shot = ss.full_screenshot(driver, save_path = ‘/Screenshot’, image_name= ‘name.png’)
# screen = Image.open(screen_shot)
# screen.show()

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d")
name_screenshot = 'screen ' + now_date + '.png'
driver.save_screenshot(name_screenshot)












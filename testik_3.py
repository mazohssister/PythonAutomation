from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # add option to selenium not to close browser after test ends
driver = webdriver.Chrome(options=chrome_options)

s = Service(r'C:\Users\sonya\PycharmProjects\PythonAutomation\chromedriver.exe')
browser = webdriver.Chrome(service=s)
base_url = 'https://www.saucedemo.com/'
browser.get(base_url)

login_standard_user = "standard"
password_for_all = "secret_sauce"

user_name = browser.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
password = browser.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(password_for_all)
print("Input password")
button_login = browser.find_element(By.XPATH, "//input[@name='login-button']")
button_login.click()
print("Click the button")

'''Check the alarm with unsuccessful registration'''
warring = browser.find_element(By.XPATH, "//h3[@data-test='error']")
text_warring = warring.text
assert text_warring == "Epic sadface: Username and password do not match any user in this service"
print("PASSED")

browser.refresh()
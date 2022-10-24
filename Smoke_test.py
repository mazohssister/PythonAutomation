"""Import some libs"""

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from Functions import *

""""Make some configurations"""
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

s = Service(r'C:\Users\sonya\PycharmProjects\PythonAutomation\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# TEST DATA
login_standard_user = "standard_user"
password_for_all = "secret_sauce"
first_name_value = "Sofiia"
last_name_value = "Litvinova"
zip_code_value = "188666"

"""Make an input in Login & Password"""

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)

'''Check the sidebar menu'''
password = driver.find_element(By.XPATH, "//input[@name='password']")
password.send_keys(password_for_all)
password.submit()  # also you can use var.send_keys(Keys.RETURN OR enter) to imitate enter
print("Authorization passed")

'''Save to variables name and price of the product'''
'''INFO Product_1'''
product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[1]")
text_product_1 = product_1.text
print(text_product_1)

price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
price_product_1 = price_product_1.text
print(price_product_1)

add_to_cart_product_1 = driver.find_element(By.XPATH, "(//button[@class='btn btn_primary btn_small btn_inventory'])[1]")
add_to_cart_product_1.click()
print("Product_1 added to card")

shopping_cart_button = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
shopping_cart_button.click()
print("Open a shopping card")

# Search for cart info
shopping_cart_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[1]")
shopping_cart_text_product_1 = shopping_cart_product_1.text
assert shopping_cart_text_product_1 == text_product_1

shopping_cart_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
shopping_cart_price_product_1 = shopping_cart_price_product_1.text
assert shopping_cart_price_product_1 == price_product_1

checkout_button = driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button']")
checkout_button.click()

# PAGE. CHECKOUT: YOUR INFORMATION
first_name = driver.find_element(By.XPATH, "//input[@placeholder='First Name']")
first_name.send_keys(first_name_value)

last_name = driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
last_name.send_keys(last_name_value)

zip_code = driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']")
zip_code.send_keys(zip_code_value)

continue_button = driver.find_element(By.XPATH,
                                      "//input[@class='submit-button btn btn_primary cart_button btn_action']")
continue_button.click()

# PAGE. FINISH CHECKOUT.
finish_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_name'])[1]")
finish_text_product_1 = finish_product_1.text
assert finish_text_product_1 == text_product_1

finish_price_product_1 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[1]")
finish_price_product_1 = finish_price_product_1.text
assert finish_price_product_1 == price_product_1

item_subtotal_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
item_subtotal_price_value = leave_only_digits(item_subtotal_price.text)

tax_price = driver.find_element(By.XPATH, "//div[@class='summary_tax_label']")
tax_price_value = leave_only_digits(tax_price.text)

total_plus_tax_price = driver.find_element(By.XPATH, "//div[@class='summary_total_label']")
total_plus_tax_price_value = leave_only_digits(total_plus_tax_price.text)

print(tax_price_value)
print(total_plus_tax_price_value)
print(type(tax_price_value))
print(type(total_plus_tax_price_value))


assert float(total_plus_tax_price_value) == float(tax_price_value) + float(item_subtotal_price_value)
print("Total price is correct")

finish_button = driver.find_element(By.XPATH, "//button[@class='btn btn_action btn_medium cart_button']")
finish_button.click()

driver.quit()


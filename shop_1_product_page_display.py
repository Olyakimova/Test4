# from shop import *
# driver = get_driver()
# login_and_shop(driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

# Логин
my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()

email = driver.find_element_by_id("username")
email.send_keys("tester@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("as12DF34g")

register_btn = driver.find_element_by_css_selector("[value='Login']")
register_btn.click()

# Переход на вкладку "Shop"
shop_menu = driver.find_element_by_css_selector("#menu-item-40 > a")
shop_menu.click()

# 1. Отображение страницы товара
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")

book_html5 = driver.find_element_by_xpath("//h3[text()='HTML5 Forms']")
book_html5.click()

# Проверка что заголовок книги "HTML5 Forms"
book_name = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//h1"), "HTML5 Forms"))
print("HTML5 Forms", book_name)

driver.quit()

from selenium import webdriver
from selenium.webdriver.support.select import Select
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

# 3. Сортировка товаров

# Проверка что в селекторе выбран вариант сортировки от большего к меньшему

orderby_selector = driver.find_element_by_class_name("orderby")

orderby_selector_high_to_low = orderby_selector.get_attribute("value")

if orderby_selector_high_to_low == "price-desc":
    print("В селекторе выбран вариант сортировки от большего к меньшему")
else:
    print("В селекторе выбран другой вариант сортировки: ",
          orderby_selector_high_to_low)

# Cортировка товаров от большего к меньшему

select = Select(orderby_selector)
select.select_by_value("price-desc")

# Вторая проверка что в селекторе выбран вариант сортировки от большего к меньшему

orderby_selector = driver.find_element_by_class_name("orderby")

high_to_low_check = orderby_selector.get_attribute("value")

if high_to_low_check == "price-desc":
    print("В селекторе выбран вариант сортировки от большего к меньшему")
else:
    print("В селекторе выбран другой вариант сортировки: ",
          high_to_low_check)

driver.quit()

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

# 2. Количество товаров в категории
time.sleep(3)
#  Переход в категорию "HTML"
categories_html = driver.find_element_by_xpath("//a[text()='HTML']")
categories_html.click()

# Проверка что отображается три товара

items_count = driver.find_elements_by_css_selector("li.product.type-product")

if len(items_count) == 3:
    print("В разделе 3 товара")
else:
    print("Ошибка. Количество товаров в разделе: " + str(len(items_count)))

driver.quit()

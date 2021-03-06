from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

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

# 4. Oтображение, скидка товара

# Переход в карточку товара книга "Android Quick Start Guide"
book_android = driver.find_element_by_xpath(
    "//h3[text()='Android Quick Start Guide']")
book_android.click()

# Проверка что содержимое старой цены = "₹600.00"
del_price = driver.find_element_by_css_selector(
    ".price del .woocommerce-Price-amount")
del_price_get_text = del_price.text
assert del_price_get_text == "₹600.00"

# Проверка что содержимое новой цены = "₹450.00"
ins_price = driver.find_element_by_css_selector(
    ".price ins .woocommerce-Price-amount")
ins_price_get_text = ins_price.text
assert ins_price_get_text == "₹450.00"

# Открытие обложки книги в окне предпросмотра картинки
img = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[alt='Android Quick Start Guide']")))
img.click()

close_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.pp_close")))
close_btn.click()

driver.quit()

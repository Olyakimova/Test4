from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

# Переход на вкладку "Shop"
shop_menu = driver.find_element_by_css_selector("#menu-item-40 > a")
shop_menu.click()

#  5. Проверка цены в корзине

time.sleep(2)
driver.execute_script("window.scrollBy(0, 400);")

# Добавление товара в корзину
add_to_basket = driver.find_element_by_css_selector("[data-product_id='182']")
add_to_basket.click()

time.sleep(2)
#  Проверка что возле корзины (вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
cart_contents = driver.find_element_by_css_selector(".cartcontents")
cart_contents_get_text = cart_contents.text
assert cart_contents_get_text == "1 Item"

cart_amount = driver.find_element_by_css_selector(
    ".wpmenucart-contents .amount")
cart_amount_get_text = cart_amount.text
assert cart_amount_get_text == "₹180.00"

# Переход в корзину
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click()

# Проверка что в Subtotal и в Total отобразилась стоимость
subtotal = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "woocommerce-Price-amount"), "₹180.00"))
print("subtotal ", subtotal)

total = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount.amount"), "₹189.00"))
print("total ", total)

driver.quit()

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

# Переход на вкладку "Shop"
shop_menu = driver.find_element_by_css_selector("#menu-item-40 > a")
shop_menu.click()

#  6. Работа в корзине

time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")

# Добавление товара в корзину
html5_webApp_develpment_book = driver.find_element_by_css_selector(
    "[data-product_id='182']")
html5_webApp_develpment_book.click()

time.sleep(2)

mastering_javaScript_book = driver.find_element_by_css_selector(
    "[data-product_id='165']")
mastering_javaScript_book.click()

# Переход в корзину
time.sleep(2)
driver.find_element_by_css_selector("a.wpmenucart-contents").click()

# Работа в корзине
time.sleep(2)
html5_webApp_develpment_book_remove = driver.find_element_by_css_selector(
    ".cart tbody :nth-child(1) .remove")
html5_webApp_develpment_book_remove.click()

undo = driver.find_element_by_xpath("//a[text()='Undo?']")
undo.click()

quantity = driver.find_element_by_css_selector(
    "[name='cart[9766527f2b5d3e95d4a733fcfb77bd7e][qty]']")
quantity.clear()
quantity.send_keys(3)

update_basket = driver.find_element_by_css_selector("[name='update_cart']")
update_basket.click()

# Проверка что value элемента quantity для "Mastering JavaScript" равно 3
quantity_check = quantity.get_attribute("value")
assert quantity_check == "3"

time.sleep(3)
apply_coupon = driver.find_element_by_css_selector("[name='apply_coupon']")
apply_coupon.click()

# Проверка что возникло сообщение: "Please enter a coupon code."
message = driver.find_element_by_css_selector(".woocommerce-error li")
message_get_text = message.text
assert message_get_text == "Please enter a coupon code."

driver.quit()

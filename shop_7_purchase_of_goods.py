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

#  7. Покупка товара

time.sleep(3)
driver.execute_script("window.scrollBy(0, 300);")

# Добавление товара в корзину
html5_webApp_develpment_book = driver.find_element_by_css_selector(
    "[data-product_id='182']")
html5_webApp_develpment_book.click()
time.sleep(3)

# Переход в корзину
time.sleep(3)
driver.find_element_by_css_selector("a.wpmenucart-contents").click()

proceed_to_checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button.button.alt.wc-forward")))
proceed_to_checkout.click()

# Заполнение всех обязательных полей

first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Olga")

last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Yakimova")

email = driver.find_element_by_id("billing_email")
email.send_keys("tester@gmail.com")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("1234567890")

country = driver.find_element_by_id("s2id_billing_country")
country.click()

country_input = driver.find_element_by_id("s2id_autogen1_search")
country_input.send_keys("Russia")

country_select = driver.find_element_by_css_selector(
    "div.select2-result-label .select2-match")
# :nth-child(182) id - #select2-result-label-2457 select2-result-label-2914  # //div[text() = 'Russia']
country_select.click()

address = driver.find_element_by_id("billing_address_1")
address.send_keys("Nevsky prospect")

city = driver.find_element_by_id("billing_city")
city.send_keys("Sankt-Peterburg")

state = driver.find_element_by_id("billing_state")
state.send_keys("Len oblast")

postcode = driver.find_element_by_id("billing_postcode")
postcode.send_keys("192168")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)

check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()

place_order = driver.find_element_by_id("place_order")
place_order.click()

#  Проверка что отображается надпись "Thank you. Your order has been received."
message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"),
        "Thank you. Your order has been received."))
print("message ", message)

# Проверка что в Payment Method отображается текст "Check Payments"
payment_method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.XPATH, "//td[text()='Check Payments']"), "Check Payments"))
print("payment_method ", payment_method)

driver.quit()

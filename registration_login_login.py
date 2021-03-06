from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")

# Переход на вкладку "My Account Menu"
my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()

# "Логин"
email = driver.find_element_by_id("username")
email.send_keys("tester@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("as12DF34g")

login_btn = driver.find_element_by_css_selector("[value='Login']")
login_btn.click()

# Проверка что на странице есть элемент "Logout"

logout_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout"), "Logout"))
print("Logout", logout_element)

driver.quit()

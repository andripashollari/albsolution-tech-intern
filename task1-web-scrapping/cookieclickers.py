from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
sys.path.insert(0, "./local_lib")

from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://orteil.dashnet.org/cookieclicker/"
driver.uc_open_with_reconnect(url, 4)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

driver.uc_gui_click_captcha()
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"


WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookie_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i))

        if not product_price.text.isdigit():
            continue

        product_price = int(product_price.text)

        if cookie_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

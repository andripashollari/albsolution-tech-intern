from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://prodotti.metro.it/shop/category/alimentare/"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()
time.sleep(5)
shadow_host = driver.find_element(By.TAG_NAME, "cms-cookie-disclaimer")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
accept_btn = shadow_root.find_element(By.CSS_SELECTOR, "button.accept-btn")
driver.execute_script("arguments[0].click();", accept_btn)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "mfcss_card-article-2--grid-container-flex"))
)
count = 0
max_count = driver.find_element(By.CLASS_NAME, "text-default").text.split(" ")[4]
max_count = int(max_count)
print(max_count)
while count < max_count:
    all_elements = driver.find_element(By.CLASS_NAME, "mfcss_card-article-2--grid-container-flex")
    span_elments = all_elements.find_elements(By.CLASS_NAME, "sd-articlecard")
    span_elments = span_elments[-24:]
    for e in span_elments:
        print(count)
        print(e.text)
        print("\n")
        count += 1
    extend_button = driver.find_element(By.CLASS_NAME, "mfcss_load-more-articles")
    extend_button.click()
    time.sleep(1)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

username = 'rgsrahul'
password = 'Sharma02462##'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com")

email = driver.find_element(By.NAME,'email')
time.sleep(2)
cred = driver.find_element(By.NAME,'pass')
time.sleep(2)
submit = driver.find_element(By.NAME,'login')
time.sleep(2)
email.send_keys(username)
cred.send_keys(password)
submit.click()
time.sleep(5)

search_box = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search Facebook"]'))
)
search_box.send_keys("bhavesh chauhan")
time.sleep(20)
search_box.click()


driver.quit()
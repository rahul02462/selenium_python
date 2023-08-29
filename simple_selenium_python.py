from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time



username = 'rgsrahul'
password = 'Sharma02462##'

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")

email = driver.find_element(By.NAME,'email')
cred = driver.find_element(By.NAME,'pass')
submit = driver.find_element(By.NAME,'login')

email.send_keys(username)
cred.send_keys(password)
submit.click()
time.sleep(50)

driver.close()
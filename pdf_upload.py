import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.ilovepdf.com/pdf_to_word")
time.sleep(5)

#select files
input_file = driver.find_element(By.XPATH, "//input[@type='file']")
input_file.send_keys("C:/Users/Dell/Downloads/data/National.pdf")
time.sleep(10)

##convert button
convert = WebDriverWait(driver,5).until(
    EC.visibility_of_element_located((By.ID,'processTask'))
)
Click_convert = WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.ID,'processTask'))
)
Click_convert.click()
time.sleep(40)


##ocr section
if driver.find_element(By.XPATH, "//button[contains(text(), 'Continue without OCR')]"):
    # ocr_button_click = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue without OCR')]")
    # ocr_button_click.click()
    # time.sleep(40)

##send file

driver.quit()
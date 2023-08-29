from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the Chrome driver and open WhatsApp Web
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

input("Please login or scan the code and log in")

# Wait until the search box is visible
# search_box = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, '._1biMM _3sHED'))
# )
search_box = driver.find_element(By.CLASS_NAME, '._1biMM ._3sHED')
# Send keys to the search box
search_box.send_keys("wifey")
search_box.send_keys(Keys.RETURN)

# Wait for 10 seconds to let the chat load (you can adjust the time as needed)
time.sleep(240)

# Close the browser
driver.close()

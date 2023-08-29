import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Open Amazon website
    driver.get("https://www.amazon.in/")

    # Search for the desired product
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox'))
    )
    search_box.send_keys("iphone 13")

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nav-search-submit-button'))
    )
    search_button.click()

    #driver.get("https://www.amazon.in/OnePlus-Nord-Chromatic-128GB-Storage/dp/B0BY8MCQ9S/ref=sr_1_1?crid=8N750QWK8VG7&keywords=oneplus&qid=1691851433&sprefix=one+plu%2Caps%2C203&sr=8-1")


    # Wait for the product list to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-result-item"))
    )

    desired_product = 'Apple iPhone 13 (128GB) - Blue'

    # Find all product items
    product_items = driver.find_elements(By.CSS_SELECTOR, ".s-line-clamp-2")

    # Scroll to find the desired product and click on it
    for item in product_items:
        product_name = item.text
        if desired_product in product_name:
            driver.execute_script("arguments[0].scrollIntoView();", item)
            item.click()
            break

    # Wait for the product page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'submit.add-to-cart'))
    )

    # Add the product to the cart
    add_to_cart_button = driver.find_element(By.ID, 'submit.add-to-cart')
    add_to_cart_button.click()
    time.sleep(50)

    # # Wait for the cart page to load
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'hlb-ptc-btn-native'))
    # )

    # Proceed to checkout
    # checkout_button = driver.find_element(By.ID, 'hlb-ptc-btn-native')
    # checkout_button.click()

    # You may need to handle the checkout process as per your requirements

finally:
    # Close the browser
    driver.quit()

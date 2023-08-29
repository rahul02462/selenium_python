from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def automate_google_search(search_query):
    # Specify the path to the Chrome WebDriver executable
    # Make sure you have installed ChromeDriver and its path is in the system environment variable
    driver = webdriver.Chrome()

    # Open Google's search page
    driver.get("https://www.google.com")

    # Find the search box and enter the search query
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(3)

    # Retrieve the search results
    search_results = driver.find_elements_by_xpath("//div[@class='tF2Cxc']")
    for result in search_results:
        print(result.text)
        print('-' * 50)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    automate_google_search(search_query)

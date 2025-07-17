from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

BASE_QUERY = "dhsadsam"
NUM_SEARCHES = 30

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bing.com")

for i in range(1, NUM_SEARCHES + 1):
    query = f"{BASE_QUERY}{i}"
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()
    print(f"Searched: {query}")
    time.sleep(random.uniform(4.5, 7.0))  # Wait between 4.5 and 7 seconds

driver.quit()

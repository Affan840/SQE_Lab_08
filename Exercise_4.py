
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open login page
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

# Locate username field using ID
username_id = driver.find_element(By.ID, "username")
print("Username field found using ID.")

# Locate username field using NAME
username_name = driver.find_element(By.NAME, "username")
print("Username field found using NAME.")

# Locate username field using CSS Selector
username_css = driver.find_element(By.CSS_SELECTOR, "input#username")
print("Username field found using CSS SELECTOR.")

# Close browser
driver.quit()

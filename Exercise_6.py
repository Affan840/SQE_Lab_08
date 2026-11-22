
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open webpage containing a table
driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)

# Locate the 2nd td inside the 3rd tr using XPath
cell = driver.find_element(
    By.XPATH, "(//table[@id='table1']//tr)[3]/td[2]"
)

# Print the located cell's text
print("Located cell text:", cell.text)

# Close browser
driver.quit()

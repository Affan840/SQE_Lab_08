
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome
driver = webdriver.Chrome()

# Open Wikipedia
driver.get("https://www.wikipedia.org")

# Find all links using Tag Name
links = driver.find_elements(By.TAG_NAME, "a")

# Print total number of links
print("Total links on Wikipedia:", len(links))

# Close browser
driver.quit()

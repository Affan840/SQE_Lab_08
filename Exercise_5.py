
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open a page containing a form
driver.get("https://www.w3schools.com/html/html_forms.asp")
time.sleep(2)

# Find all text input elements using CSS Selector
text_inputs = driver.find_elements(
    By.CSS_SELECTOR, "input[type='text']"
)

# Print total number of matching elements
print("Total text inputs found:", len(text_inputs))

# Print identifying attributes of each input
for index, element in enumerate(text_inputs, start=1):
    print("\nInput", index)
    print("Name:", element.get_attribute("name"))
    print("ID:", element.get_attribute("id"))

# Close browser
driver.quit()

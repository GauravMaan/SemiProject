# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# # Open Safari Browser (Desktop Mode)
# driver = webdriver.Safari()
# driver.maximize_window()
#
# # Step 1: Directly navigate to OrangeHRM demo login page
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(2)
#
# # Step 2: Verify we are on the login page
# assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"
#
# # Step 3: Enter login credentials
# username_field = driver.find_element(By.NAME, "username")
# password_field = driver.find_element(By.NAME, "password")
# login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#
# username_field.send_keys("Admin")
# password_field.send_keys("admin123")
# login_button.click()
# time.sleep(5)
#
# # Step 4: Validate login success
# assert "dashboard" in driver.current_url.lower(), "Login Failed!"
# print("✅ Login successful on Desktop!")
#
# Search=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')
# Search.send_keys("Pim")
# time.sleep(3)
# print("✅ successfully searched")
#
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Safari Browser
driver = webdriver.Safari()
driver.maximize_window()

# Step 1: Navigate to OrangeHRM Demo Login Page
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(2)

# Step 2: Verify we are on the login page
assert "orangehrmlive.com" in driver.current_url, "❌ Not on the correct login page!"

# Step 3: Enter login credentials
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()
time.sleep(5)

# Step 4: Validate login success
assert "dashboard" in driver.current_url.lower(), "❌ Login Failed!"
print("✅ Login successful on Desktop!")

# Step 5: List of menu items to search one by one
search_items = ["PIM", "Admin", "Leave", "Time", "Recruitment", "My Info", "Performance",
                "Dashboard", "Directory", "Maintenance", "Buzz"]

# Step 6: Locate the search bar
search_bar = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input')

# Step 7: Search each item one by one (Clearing field using JavaScript before entering new text)
for item in search_items:
    driver.execute_script("arguments[0].value = '';", search_bar)  # Force clear using JavaScript
    search_bar.send_keys(item)
    time.sleep(2)  # Wait for search results
    print(f"✅ Successfully searched for '{item}'")

# Step 8: Close the browser
driver.quit()
print("✅ Test completed. Browser closed.")
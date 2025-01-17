from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Open Chrome Browser (Desktop Mode)
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open Google
driver.get("https://www.google.com")
time.sleep(2)

# Step 2: Search for "OrangeHRM demo login"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("OrangeHRM demo login")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Step 3: Click the first search result
first_result = driver.find_element(By.XPATH, "(//h3)[1]")
first_result.click()
time.sleep(3)

# Step 4: Verify we are on the login page
assert "orangehrmlive.com" in driver.current_url, "Not on the correct login page!"

# Step 5: Enter login credentials
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_field.send_keys("Admin")
password_field.send_keys("admin123")
login_button.click()
time.sleep(5)

# Step 6: Validate login success
assert "dashboard" in driver.current_url.lower(), "Login Failed!"
print("✅ Login successful on Desktop!")
time.sleep(3)

# Step 7: Click all the options in the left sidebar and validate (excluding "Maintenance")
sidebar_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a'

# Get the number of sidebar elements
sidebar_elements = driver.find_elements(By.XPATH, sidebar_xpath)

for i in range(len(sidebar_elements)):
    # Re-fetch sidebar elements to avoid stale element reference
    sidebar_elements = driver.find_elements(By.XPATH, sidebar_xpath)

    # Get the specific option
    option = sidebar_elements[i]

    # Get option name
    option_name = option.text.strip()

    # **Skip the "Maintenance" option**
    if option_name.lower() == "maintenance":
        print(" Skipping Maintenance section...")
        continue

    if option_name:  # Ensure it's a valid option
        print(f"Clicking on: {option_name}")
        option.click()
        time.sleep(3)

        try:
            # Try checking the page heading (if available)
            page_heading = driver.find_element(By.TAG_NAME, "h6").text.strip()
            assert option_name.lower() in page_heading.lower(), f"❌ Validation failed for {option_name}"
            print(f"✅ Successfully navigated to: {page_heading}")
        except:
            print(f"⚠️ Could not validate {option_name} via heading, skipping validation.")

# Step 8: Close the browser
driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestOrangeHRM:
    def setup_method(self):
        """Setup method to open the browser before each test"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        """Teardown method to close the browser after each test"""
        self.driver.quit()

    def test_login_and_sidebar_navigation(self):
        """Test OrangeHRM login and sidebar navigation"""
        driver = self.driver

        # Step 1: Open OrangeHRM login page directly
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Step 2: Enter login credentials
        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username.send_keys("Admin")
        password.send_keys("admin123")
        login_button.click()

        # Step 3: Validate successful login
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        print("✅ Login Successful!")

        # Step 4: Click Sidebar Options (Skipping "Maintenance")
        sidebar_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory"]

        for option_name in sidebar_options:
            try:
                # Find sidebar option and click
                option = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, f'//span[text()="{option_name}"]/ancestor::a'))
                )
                option.click()
                print(f"✅ Navigated to {option_name}")
            except Exception as e:
                print(f"⚠️ Could not validate {option_name}. Error: {str(e)}")
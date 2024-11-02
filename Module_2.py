from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def open_url(self):
#TO Open the login page URL
        self.driver.get(self.base_url)



    def login(self, username, password):
#To Log in to OrangeHRM with the given username and password
        try:
            username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button.click()
            print("Logged in successfully.")
        except TimeoutException:
            print("Failed to log in due to a timeout.")




    def navigate_to_admin_page(self):
        """Navigate to the Admin page."""
        try:
            admin_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
            admin_tab.click()
            print("Navigated to Admin page.")
        except TimeoutException:
            print("Failed to navigate to Admin page.")




    def validate_menu_options(self, expected_options):
#To Validate the presence of menu options on the Admin page
        missing_options = []
        for option in expected_options:
            try:
                # To Check if the option is present in the side pane
                self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{option}']")))
                print(f"Menu option '{option}' is present on the Admin page.")
            except TimeoutException:
                print(f"Menu option '{option}' is missing on the Admin page.")
                missing_options.append(option)

        if not missing_options:
            print("All specified menu options are present on the Admin page.")
        else:
            print(f"The following menu options are missing: {missing_options}")




def main():
#To initialize WebDriver
    driver = webdriver.Chrome()

    try:
#To  Initialize the OrangeHRM class with the driver
        orange_hrm = OrangeHRM(driver)

#To  Open URL and perform login
        orange_hrm.open_url()
        orange_hrm.login("Admin", "admin123")

#To  Navigate to Admin page
        orange_hrm.navigate_to_admin_page()

#TO  Validate specific menu options on the Admin page
        expected_menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
        orange_hrm.validate_menu_options(expected_menu_options)

    finally:
    # Close the browser after the test
        driver.quit()


if __name__ == "__main__":
    main()


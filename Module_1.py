from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchWindowException


class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        self.base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


    def open_url(self):
    #Open the login page URL
        if self.is_window_open():
            self.driver.get(self.base_url)


    def login(self, username, password):
        #Log in to OrangeHRM with the given username and password
        if self.is_window_open():

            try:
                username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
                password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
                login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

                username_field.send_keys(username)
                password_field.send_keys(password)
                login_button.click()
                print("Logged in successfully.")
            except TimeoutException:
                print("Failed to login")
            except NoSuchWindowException:
                print("Browser window closed during login")



    def navigate_to_admin_page(self):
    #Navigate to the Admin page
        if self.is_window_open():
            try:
                admin_tab = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']")))
                admin_tab.click()
                print("Navigated to Admin page")
            except TimeoutException:
                print("Failed to navigate to Admin page")
            except NoSuchWindowException:
                print("Browser window closed during navigation")



    def validate_admin_page_title(self, expected_title):
        #To Validate the title of the Admin page
        if self.is_window_open():
            try:
                self.wait.until(lambda driver: driver.title == expected_title)
                print("Page title is correct: '{expected_title}'")
            except TimeoutException:
                print("Failed to validate page title")
            except NoSuchWindowException:
                print("Browser window closed during title validation")




    def validate_admin_page_options(self, options):

        #To Validate the presence of specified options on the Admin page
        if self.is_window_open():
            missing_options = []
            for option in options:
                if self.is_window_open():
                    try:
                        # Validate Nationalities and Corporate Branding with XPath
                        if option == "Nationalities":
                            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Nationalities']")))
                        elif option == "Corporate Branding":
                            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Corporate Branding']")))
                        else:
                            # Using partial text matching for other options
                            self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[contains(text(), '{option}')]")))
                        print(f"Option '{option}' is present on the Admin page.")
                    except TimeoutException:
                        print(f"Option '{option}' is missing on the Admin page.")
                        missing_options.append(option)
                    except NoSuchWindowException:
                        print("Browser window closed while validating options.")
                        break

            if not missing_options:
                print("All specified options are present on the Admin page.")
            else:
                print(f"The following options are missing: {missing_options}")




    def is_window_open(self):
    #To Check if the browser window is still open
        try:
            self.driver.current_window_handle
            return True
        except NoSuchWindowException:
            print("Browser window has been closed.")
            return False




def main():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        # Initialize the OrangeHRM class with the driver
        orange_hrm = OrangeHRM(driver)

    # Open URL and perform login
        orange_hrm.open_url()
        orange_hrm.login("Admin", "admin123")

    # Navigate to Admin page and validate title
        orange_hrm.navigate_to_admin_page()
        orange_hrm.validate_admin_page_title("OrangeHRM")

    # Validate specific options on the Admin page
        options_to_validate = ["User Management", "Job", "Organization", "Qualifications",
                               "Nationalities",  # Using XPath
                               "Corporate Branding",  # Using XPath
                               "Configuration"]
        orange_hrm.validate_admin_page_options(options_to_validate)

    finally:
    # Close the browser after the test
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()


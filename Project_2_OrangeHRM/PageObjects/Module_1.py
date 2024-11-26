
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Data class to store application-specific data such as URLs and credentials.
class Data1:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"


# Locators class to store element locators for the application.
class Locators1:
    username_locator = (By.NAME, "username")
    password_locator = (By.NAME, "password")
    login_locator = (By.XPATH, "//button[@type='submit']")
    admin_locator = (By.XPATH, "//span[text()='Admin']")
    admin_options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Branding", "Configuration"]
    menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory",
                    "Maintenance", "Buzz"]


# Main class to define methods for interacting with the Webpage.
class Module1(Data1, Locators1):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    #Method to open URL in the browser.
    def open_url(self):
        self.driver.get(self.url)
        print(f"Opened URL: {self.driver.current_url}")
        if self.driver.title == "OrangeHRM":
            print("Title Matched", self.driver.title)
            return True
        else:
            return False

    #Method to login with valid credentials.
    def login(self):
        try:
            username_element = self.wait.until(EC.element_to_be_clickable(self.username_locator))
            username_element.send_keys(self.username)
            print(f"Entered Username: {self.username}")

            password_element = self.wait.until(EC.element_to_be_clickable(self.password_locator))
            password_element.send_keys(self.password)
            print(f"Entered Password: {self.password}")

            login_element = self.wait.until(EC.element_to_be_clickable(self.login_locator))
            login_element.click()
            print("Logged in successfully")
            return True
        except TimeoutException:
            return False

    #Method to Navigate to Admin page.
    def navigate_to_admin(self):
        try:
            admin_element = self.wait.until(EC.element_to_be_clickable(self.admin_locator))
            admin_element.click()
            print("Navigated to Admin page")
            return True
        except TimeoutException:
            return False


    #Method to validate whether the given options are present and enabled in the Admin page.
    def admin_page_options(self):
        missing_options = []
        for option in self.admin_options:
            try:
                if option == "Nationalities":
                   self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Nationalities']")))
                elif option == "Corporate Branding":
                    self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Corporate Branding']")))
                else:
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{option}']")))
                print(f"Option '{option}' is present on the Admin page.")
            except TimeoutException:
                print(f"Option '{option}' is missing on the Admin page.")
                break

        if not missing_options:
            print("All specified options are present on the Admin page.")
            return True
        else:
            print(f"The following options are missing: {missing_options}")
            return False


    def quit(self):
        self.driver.quit()






from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Data:
    username = "Admin"
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

class Locators:
    forgot_password_locator = (By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")
    username_locator = (By.NAME, "username")
    reset_button_locator = (By.XPATH, "//button[@type='submit']")
    success_message_locator = (By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]")

class Homepage(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self):
        self.driver.get(self.url)
        print(f"Opened URL: {self.driver.current_url}")
        if self.driver.title == "OrangeHRM":
            return True
        else:
            return False


    def click_forgot_password(self):
        try:

            forgot_password_element = self.wait.until(EC.element_to_be_clickable(self.forgot_password_locator))
            forgot_password_element.click()
            print("Clicked on Forgot Password")
            return True
        except TimeoutException:
            return False


    def reset_password(self):
        try:
            username_element = self.wait.until(EC.element_to_be_clickable(self.username_locator))
            username_element.send_keys(self.username)
            print(f"Entered Username: {self.username}")

            reset_button_element = self.wait.until(EC.element_to_be_clickable(self.reset_button_locator))
            reset_button_element.click()
            print("Clicked on Reset Password")

            try:
                success_message_element = self.wait.until(EC.element_to_be_clickable(self.success_message_locator))
                print("Success Message Displayed ->", success_message_element.text)
                self.wait = WebDriverWait(self.driver, 10)

            except TimeoutException:
                self.wait.until(lambda driver: "Reset Password link sent successfully" in driver.page_source)
                print("Test Passed - Reset Password link sent successfully")
            return True

        except TimeoutException:
            return False


        finally:
            self.driver.quit()


if __name__ == "__main__":
    homepage = Homepage()
    homepage.open_url()
    homepage.click_forgot_password()
    homepage.reset_password()
    homepage.driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class OrangeHRM:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 15)
        self.base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def open_url(self):
        #To open the login page URL
        self.driver.get(self.base_url)

    def click_forgot_password(self):
        #To click on Forgot your password
        try:
            forgot_password_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p")))
            forgot_password_link.click()
            print("Clicked on 'Forgot your password?' link.")
        except TimeoutException:
            print("Failed to find 'Forgot your password?' link.")

    def reset_password(self, username):
        #To enter username and reset password, then validate success message
        try:
            username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            username_field.send_keys(username)
            print("Entered username: {username}")

            reset_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
            reset_button.click()
            print("Clicked on Reset Password button.")

            #Checking if success message appears as visible element
            try:
                success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[1]/div/form/div[2]/button[2]")))

                print("Test Passed: Success message displayed ->", success_message.text)
                self.wait = WebDriverWait(self.driver, 15)

            except TimeoutException:
                self.wait.until(lambda driver: "Reset Password link sent successfully" in driver.page_source)

                print("Test Passed: Success message found in page source.")

        except TimeoutException:
            print("Test Failed: Reset password process failed due to timeout.")
        except Exception as e:
            print("Test Failed: An unexpected error occurred - {e}")


def main():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        # Initialize the OrangeHRM class with the driver
        orange_hrm = OrangeHRM(driver)

        # Open URL and test forgot password functionality
        orange_hrm.open_url()
        orange_hrm.click_forgot_password()
        orange_hrm.reset_password("Admin")

    finally:
        # Close the browser after the test
        driver.quit()


if __name__ == "__main__":
    main()


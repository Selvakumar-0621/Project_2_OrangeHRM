import pytest
from selenium.webdriver.common.devtools.v128.fed_cm import open_url
from webdriver_manager.core import driver
from PageObjects import Homepage
from PageObjects.Homepage import Homepage, Data

homepage = Homepage()

self = homepage.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


#Test Open URL
def test_open_url():
    assert homepage.open_url() == True
    print("Test Open URL - Passed")


#Test Click Forgot Password
def test_click_forgot_password():
    assert homepage.click_forgot_password() == True
    print("Test Click Forgot Password - Passed")


#Test Click Reset password
def test_reset_password():
    assert homepage.reset_password() == True
    print("Test Reset Password - Passed")




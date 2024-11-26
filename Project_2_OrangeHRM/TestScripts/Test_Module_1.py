from PageObjects.Module_1 import Module1

#Global setup to initialize Homepage instance
module1 = Module1()

self = module1.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Test Open URL
def test_open_url():

    assert module1.open_url() == True
    print("Test Open URL - Passed")


#Test Login
def test_login():
    assert module1.login() == True
    print("Test Login - Passed")


#Test Navigation to Admin page
def test_navigate_to_admin():
    assert module1.navigate_to_admin() == True
    print("Test Navigation to Admin page - Passed")


#Test Admin Page options
def test_admin_page_options():
    assert module1.admin_page_options() == True
    print("Test Admin Page options - Passed")
    module1.quit()


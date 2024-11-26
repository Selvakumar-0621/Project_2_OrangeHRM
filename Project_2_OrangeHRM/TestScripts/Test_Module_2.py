from PageObjects.Module_2 import Module2

#Global setup to initialize Homepage instance
module2 = Module2()
self = module2.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


#Test Open URL
def test_open_url():
    assert module2.open_url() == True
    print("Test Open URL - Passed")


#Test Login
def test_login():
    assert module2.login() == True
    print("Test Login - Passed")


#Test Navigation to Admin page
def test_navigate_to_admin():
    assert module2.navigate_to_admin() == True
    print("Test Navigation to Admin page - Passed")


#Test Admin Page options
def test_validate_menu_options():
    assert module2.validate_menu_options() == True
    print("Test Admin Page Menus - Passed")
    module2.quit()

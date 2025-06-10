import time
from utils.data_loader import load_login_data
from pages.login_page import LoginPage

login_data = load_login_data()
valid = login_data['valid']
invalid = login_data['invalid']

def test_username_required(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["empty_username"]
    login_page.login(creds["username"], creds["password"])
    assert "Username is required" in login_page.get_error_message()

def test_password_required(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["empty_password"]
    login_page.login(creds["username"], creds["password"])
    assert "Password is required" in login_page.get_error_message()

def test_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["wrong_both"]
    login_page.login(creds["username"], creds["password"])
    assert "Username and password do not match" in login_page.get_error_message()

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["locked_out"]
    login_page.login(creds["username"], creds["password"])
    assert "Sorry, this user has been locked out." in login_page.get_error_message()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = valid["standard_user"]
    login_page.login(creds["username"], creds["password"])
    assert login_page.is_logged_in()



# from pages.login_page import LoginPage
# def test_login_page_ui_elements(login_page):
#     assert login_page.get_username_placeholder() == "Username"
#     assert login_page.get_password_placeholder() == "Password"
#     assert login_page.get_login_button_text() == "Login"

# def test_username_required(login_page):
#     login_page.login("", "secret_sauce")
#     assert "Username is required" in login_page.get_error_message()

# def test_password_required(login_page):
#     login_page.login("standard_user", "")
#     assert "Password is required" in login_page.get_error_message()

# def test_invalid_credentials(login_page):
#     login_page.login("wrong_user", "wrong_pass")
#     assert "Username and password do not match" in login_page.get_error_message()

# def test_locked_out_user(login_page):
#     login_page.login("locked_out_user", "secret_sauce")
#     assert "Sorry, this user has been locked out." in login_page.get_error_message()

# def test_valid_login(login_page):
#     login_page.login("standard_user", "secret_sauce")
#     assert login_page.is_logged_in()

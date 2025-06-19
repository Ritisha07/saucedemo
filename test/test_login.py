import time
import pytest
from utils.data_loader import load_login_data
from utils.data_loader import get_valid_login_data
from pages.login_page import LoginPage

login_data = load_login_data()
valid = login_data['valid']
invalid = login_data['invalid']

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username, password", get_valid_login_data())

def test_valid_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    login_page.login(username, password)
    # the credential come from parameter we remove the below code
    # creds = valid["standard_user"]
    # login_page.login(creds["username"], creds["password"])
    assert login_page.is_logged_in()

@pytest.mark.negative
def test_username_required(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["empty_username"]
    login_page.login(creds["username"], creds["password"])
    assert "Username is required" in login_page.get_error_message()

@pytest.mark.negative
def test_password_required(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["empty_password"]
    login_page.login(creds["username"], creds["password"])
    assert "Password is required" in login_page.get_error_message()

@pytest.mark.negative
def test_invalid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["wrong_both"]
    login_page.login(creds["username"], creds["password"])
    assert "Username and password do not match" in login_page.get_error_message()

@pytest.mark.negative
def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(1)
    
    creds = invalid["locked_out"]
    login_page.login(creds["username"], creds["password"])
    assert "Sorry, this user has been locked out." in login_page.get_error_message()



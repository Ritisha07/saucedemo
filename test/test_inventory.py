import time
import pytest
from utils.data_loader import load_login_data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Load one default valid user for shared login in smoke/regression tests
default_creds = load_login_data()["valid"]["standard_user"]
default_username = default_creds["username"]
default_password = default_creds["password"]

# For parameterized test
login_data = load_login_data()["valid"]
valid_users = [(v["username"], v["password"]) for v in login_data.values()]

# Helper function
def login_and_return_inventory(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    time.sleep(1)
    return InventoryPage(driver)

@pytest.mark.parametrize("username,password", valid_users)
def test_login_with_valid_users(driver, username, password):
    inventory = login_and_return_inventory(driver, username, password)
    assert "inventory" in inventory.get_current_url()

@pytest.mark.smoke
def test_verify_title(driver):
    inventory = login_and_return_inventory(driver, default_username, default_password)
    assert inventory.get_title_text() == "Products", "Page title does not match 'Products'"

@pytest.mark.regression
def test_verify_product_count(driver):
    inventory = login_and_return_inventory(driver, default_username, default_password)
    actual_count = inventory.get_inventory_items_count()
    print(f"Actual product count found: {actual_count}")
    assert actual_count == 6, f"Expected 6 products on the page but found {actual_count}"

@pytest.mark.smoke
def test_verify_url(driver):
    inventory = login_and_return_inventory(driver, default_username, default_password)
    current_url = inventory.get_current_url()
    assert "inventory.html" in current_url, "'inventory.html' not in URL"
    assert "saucedemo.com" in current_url, "'saucedemo.com' not in URL"

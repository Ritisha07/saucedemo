import time
from utils.data_loader import load_login_data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def login_and_return_inventory(driver):
    creds = load_login_data()["valid"]["standard_user"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(creds["username"], creds["password"])
    time.sleep(1)
    return InventoryPage(driver)

def test_verify_title(driver):
    products = login_and_return_inventory(driver)
    assert products.get_title_text() == "Products", "Page title does not match 'Products'"

def test_verify_product_count(driver):
    products = login_and_return_inventory(driver)
    actual_count = products.get_inventory_items_count()
    print(f"Actual product count found: {actual_count}")
    assert actual_count == 6, f"Expected 6 products on the page but found {actual_count}"

def test_verify_url(driver):
    products = login_and_return_inventory(driver)
    current_url = products.get_current_url()
    assert "inventory.html" in current_url, "'inventory.html' not in URL"
    assert "saucedemo.com" in current_url, "'saucedemo.com' not in URL"

import time
import pytest
from utils.data_loader import load_login_data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.AddToCartPage import AddToCartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_return_cart(driver):
    creds = load_login_data()["valid"]["standard_user"]
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(creds["username"], creds["password"])
    time.sleep(1)
    return AddToCartPage(driver)

@pytest.mark.smoke
def test_add_single_item_to_cart(driver):
    cart_page = login_and_return_cart(driver)
    cart_page.add_item_to_cart_by_index(0)
    assert cart_page.get_cart_count() == 1

@pytest.mark.regression
def test_cart_item_count(driver):
    cart_page = login_and_return_cart(driver)
    cart_page.add_items(2)
    assert cart_page.get_cart_count() == 2

@pytest.mark.regression
def test_remove_product_decreases_cart_count(driver):
    cart_page = login_and_return_cart(driver)
    cart_page.add_items(2)
    assert cart_page.get_cart_count() == 2

    cart_page.go_to_cart()
    cart_page.remove_first_item()
    cart_page.continue_shopping()
    assert cart_page.get_cart_count() == 1

@pytest.mark.regression
def test_cart_total_price_correct(driver):
    cart_page = login_and_return_cart(driver)
    for i in range(3):
        cart_page.add_item_to_cart_by_index(i)
    cart_page.go_to_cart()
    cart_page.checkout_step_one("Ritisha", "Shrestha", "12345")

    prices = cart_page.get_cart_item_prices()
    expected_total = sum(prices)
    actual_total = cart_page.get_cart_total_price()
    assert actual_total == expected_total, f"Expected total {expected_total} but got {actual_total}"

@pytest.mark.smoke
def test_proceed_to_checkout(driver):
    cart_page = login_and_return_cart(driver)
    cart_page.add_items(1)
    cart_page.go_to_cart()
    cart_page.checkout_step_one("Ritisha", "Shrestha", "12345")
    assert "checkout-step-two" in driver.current_url

@pytest.mark.regression
def test_cart_is_empty_after_checkout(driver):
    cart_page = login_and_return_cart(driver)
    cart_page.add_items(2)
    cart_page.go_to_cart()
    cart_page.checkout_step_one("Ritisha", "Shrestha", "12345")
    cart_page.finish_checkout()
    WebDriverWait(driver, 10).until(EC.url_contains("checkout-complete"))
    cart_count_after_checkout = cart_page.get_cart_count()
    assert cart_count_after_checkout == 0, f"Cart count after checkout should be 0 but was {cart_count_after_checkout}"

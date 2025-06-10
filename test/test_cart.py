from pages.AddToCartPage import AddToCartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_single_item_to_cart(login_and_get_products, driver):
    cart_page = AddToCartPage(driver)
    cart_page.add_item_to_cart_by_index(0)
    assert cart_page.get_cart_count() == 1


def test_cart_item_count(login_and_get_products, driver):
    cart_page = AddToCartPage(driver)
    cart_page.add_items(2)
    assert cart_page.get_cart_count() == 2


def test_remove_product_decreases_cart_count(login_and_get_products, driver):
    cart_page = AddToCartPage(driver)
    cart_page.add_items(2)
    assert cart_page.get_cart_count() == 2

    cart_page.go_to_cart()
    cart_page.remove_first_item()
    cart_page.continue_shopping()

    assert cart_page.get_cart_count() == 1

def test_cart_total_price_correct(login_and_get_products, driver):
    cart_page = AddToCartPage(driver)

    # Add multiple products
    for i in range(3):
        cart_page.add_item_to_cart_by_index(i)

    cart_page.go_to_cart()
    cart_page.checkout_step_one("Ritisha", "Shrestha", "12345")

    prices = cart_page.get_cart_item_prices()
    expected_total = sum(prices)

    actual_total = cart_page.get_cart_total_price()

    assert actual_total == expected_total, f"Expected total {expected_total} but got {actual_total}"


def test_proceed_to_checkout(login_and_get_products, driver):
    cart_page = AddToCartPage(driver)
    cart_page.add_items(1)
    cart_page.go_to_cart()

    cart_page.checkout_step_one("Ritisha", "Shrestha", "12345")

    assert "checkout-step-two" in driver.current_url


def test_cart_is_empty_after_checkout(login_and_get_products, driver):
    cart_page = AddToCartPage(driver)

    cart_page.add_items(2)
    cart_page.go_to_cart()
    cart_page.checkout_step_one("Ritisha", "Shrestha", "12345")
    cart_page.finish_checkout()

    WebDriverWait(driver, 10).until(EC.url_contains("checkout-complete"))

    cart_count_after_checkout = cart_page.get_cart_count()
    assert cart_count_after_checkout == 0, f"Cart count after checkout should be 0 but was {cart_count_after_checkout}"

from pages.inventory_page import InventoryPage

def test_verify_title(login_and_get_products):
    products: InventoryPage = login_and_get_products
    assert products.get_title_text() == "Products", "Page title does not match 'Products'"

def test_verify_product_count(login_and_get_products):
    products: InventoryPage = login_and_get_products
    actual_count = products.get_inventory_items_count()
    print(f"Actual product count found: {actual_count}")
    assert actual_count == 6, f"Expected 6 products on the page but found {actual_count}"

def test_verify_url(login_and_get_products):
    products: InventoryPage = login_and_get_products
    current_url = products.get_current_url()
    assert "inventory.html" in current_url, "'inventory.html' not in URL"
    assert "saucedemo.com" in current_url, "'saucedemo.com' not in URL"

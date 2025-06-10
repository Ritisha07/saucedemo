import pytest
import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data_loader import load_login_data  # import data loader

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# @pytest.fixture
# def login_page(driver):
#     page = LoginPage(driver)
#     page.open()
#     time.sleep(1)
#     return page

# @pytest.fixture
# def login_and_get_products(driver):
#     login_data = load_login_data()
#     creds = login_data["valid"]["standard_user"]
    
#     login_page = LoginPage(driver)
#     login_page.open()
#     login_page.login(creds["username"], creds["password"])
#     time.sleep(1)
#     return InventoryPage(driver)

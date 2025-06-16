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
import os
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)
            screenshot_file = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_file)
            # attach screenshot path to report object for pytest-html
            if 'pytest_html' in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, 'extra', [])
                html = f'<div><img src="screenshots/{item.name}.png" alt="screenshot" style="width:400px;height:200px;" onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
                rep.extra = extra



    

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

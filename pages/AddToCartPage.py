from selenium.webdriver.common.by import By
from pages.BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[starts-with(@id, 'add-to-cart')]")
    REMOVE_FROM_CART_BUTTONS = (By.XPATH, "//button[starts-with(@id, 'remove')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_TOTAL_PRICE = (By.CLASS_NAME, "summary_subtotal_label") 
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")


    def add_item_to_cart_by_index(self, index):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()

    def add_items(self, count):
        for i in range(count):
            self.add_item_to_cart_by_index(i)

    def checkout_step_one(self, first, last, postal):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def finish_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

    def remove_first_item(self):
        button = self.driver.find_element(*self.REMOVE_FROM_CART_BUTTONS)
        button.click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return int(badges[0].text) if badges else 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()

    def get_cart_item_prices(self):
        prices_elements = self.driver.find_elements(*self.CART_ITEM_PRICES)
        return [
            float(el.text.replace("$", "").strip())
            for el in prices_elements
        ]

    def get_cart_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_TOTAL_PRICE)
        )
        return float(total_element.text.split("$")[1].strip())

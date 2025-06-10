# from selenium.webdriver.common.by import By
# from pages.BasePage import BasePage
# class InventoryPage(BasePage):
#     def __init__(self,driver):
#         self.driver=driver
    
#     def get_current_url(self):
#         return self.driver.current_url

#     def get_title_text(self):
#         # return self.driver.find_element(By.CLASS_NAME, "title").text
#         return self.driver.find_element(By.XPATH, "//*[@class='title']").text


#     def get_inventory_items_count(self):
#     #   return len(self.driver.find_elements(By.CLASS_NAME, "inventory_item"))
#     #   return len(self.driver.find_elements(By.XPATH, "//*[contains(@class, 'inventory_item')]"))
#         return len(self.driver.find_elements(.XPATH, "//div[@class='Byinventory_item' and @data-test='inventory-item']"))

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class InventoryPage(BasePage):
    # Locators 
    TITLE = (By.XPATH, "//span[@class='title']")
    #INVENTORY_ITEMS = (By.XPATH, "//div[contains(@class, 'inventory_item')]")
    INVENTORY_ITEMS = (By.XPATH, "//div[contains(@class, 'inventory_item') and @data-test='inventory-item']")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[starts-with(@id, 'add-to-cart')]")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def get_title_text(self):
        return self.driver.find_element(*self.TITLE).text

    def get_inventory_items_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))
    
    # def add_product_to_cart_by_index(self, index=0):
    #     add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
    #     if index < len(add_buttons):
    #         add_buttons[index].click()
    #     else:
    #         raise IndexError(f"Add-to-cart index {index} is out of range. Only {len(add_buttons)} found.")

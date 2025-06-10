from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def verify_element_present(self, locator):
        """Returns True if element is present in DOM, else False."""
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False

    def validate_text(self, locator, expected_text):
        """Returns True if element's text matches expected_text, else False."""
        try:
            actual_text = self.get_text(locator)
            return actual_text == expected_text
        except:
            return False

    def get_element_attribute(self, locator, attribute_name):
        """Returns the value of the attribute for the element."""
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)

    def get_number_of_elements(self, locator):
        """Returns the count of elements matching the locator."""
        elements = self.find_elements(locator)
        return len(elements)

    def hover_mouse(self, locator):
        """Moves mouse over the element."""
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# class BasePage:
#     menu_id = (By.ID, "react-burger-menu-btn")
#     logout_button = (By.ID, "logout_sidebar_link")

#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     def wait_for_visibility(self, locator, timeout=10):
#         return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

#     def wait_for_clickable(self, locator, timeout=10):
#         return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

#     def wait_for_all_elements(self, locator, timeout=10):
#         return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

#     def verify_element_present(self, by, locator):
#         try:
#             self.wait.until(EC.visibility_of_element_located((by, locator)))
#             return True
#         except:
#             return False

#     def validate_text(self, by, locator, expected_text):
#         try:
#             element = self.wait.until(EC.visibility_of_element_located((by, locator)))
#             return element.text.strip() == expected_text.strip()
#         except:
#             return False

#     def get_element_attribute(self, by, locator, attribute):
#         try:
#             element = self.wait.until(EC.presence_of_element_located((by, locator)))
#             return element.get_attribute(attribute)
#         except:
#             return None

#     def get_number_of_elements(self, by, locator):
#         try:
#             return len(self.driver.find_elements(by, locator))
#         except:
#             return 0

#     def hover_mouse(self, by, locator):
#         try:
#             element = self.wait.until(EC.visibility_of_element_located((by, locator)))
#             ActionChains(self.driver).move_to_element(element).perform()
#             return True
#         except:
#             return False

#     def open_sidebar(self):
#         self.wait_for_clickable(self.menu_id).click()
#         time.sleep(1)

#     def logout(self):
#         self.wait_for_visibility(self.logout_button)
#         self.wait_for_clickable(self.logout_button).click()

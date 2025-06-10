from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Locators 
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test='error']")
    menu_button = (By.XPATH, "//div[@class='bm-burger-button']/button")
    logout_link = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    # def login(self, username, password):
    #     self.driver.find_element(*self.username_input).clear()
    #     self.driver.find_element(*self.username_input).send_keys(username)
    #     self.driver.find_element(*self.password_input).clear()
    #     self.driver.find_element(*self.password_input).send_keys(password)
    #     self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(self.username_input)).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    
    def is_logged_in(self):
        return "inventory.html" in self.driver.current_url

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def get_username_placeholder(self):
        return self.driver.find_element(*self.username_input).get_attribute("placeholder")

    def get_password_placeholder(self):
        return self.driver.find_element(*self.password_input).get_attribute("placeholder")

    def get_login_button_text(self):
        return self.driver.find_element(*self.login_button).get_attribute("value")

    def open_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.menu_button)).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_link)).click()

    def get_current_url(self):
        return self.driver.current_url

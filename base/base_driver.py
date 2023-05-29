from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    PRICES = "product-item__price"

    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def page_scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def wait_until_button_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return button

from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from TestFramework.base.base_driver import BaseDriver


class UniversalPages(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    PRICES = "product-item__price"
    PRICE_FILTER_BUTTON = "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[1]"
    LOWEST_PRICE_FIELD = "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input"
    HIGHEST_PRICE_FIELD = "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input"
    APPLY_BUTTON = "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/button[2]"

    def getPrices(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value=self.PRICES)

    def getPriceFilterButton(self):
        return self.driver.find_element(by=By.XPATH, value=self.PRICE_FILTER_BUTTON)

    def getLowestPriceField(self):
        return self.driver.find_element(by=By.XPATH, value=self.LOWEST_PRICE_FIELD)

    def getHighestPriceField(self):
        return self.driver.find_element(by=By.XPATH, value=self.HIGHEST_PRICE_FIELD)

    def getApplyButton(self):
        return self.driver.find_element(by=By.XPATH, value=self.APPLY_BUTTON)

    def expandPriceFilter(self):
        self.getPriceFilterButton().click()
        sleep(1)

    def narrowPrices(self, lowest, highest):
        self.getLowestPriceField().send_keys(Keys.CONTROL, "a")
        self.getLowestPriceField().send_keys(Keys.DELETE)
        self.getLowestPriceField().send_keys(lowest)
        sleep(1)
        self.getHighestPriceField().send_keys(Keys.CONTROL, "a")
        self.getHighestPriceField().send_keys(Keys.DELETE)
        self.getHighestPriceField().send_keys(highest)
        sleep(1)
        self.getApplyButton().click()

from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from TestFramework.base.base_driver import BaseDriver


class SearchResultsPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    EXPAND_SORT_OPTIONS_BUTTON = "pagination__item--sort-option"
    SORT_BY_PRICE_ASC_BUTTON = "//*[@id='sort-select-1']/label[5]"
    SORT_BY_PRICE_DESC_BUTTON = "/html/body/div[1]/main/div[3]/div/div[1]/div/div[1]/div/form/div/div/label[6]"
    # ITEMS_PRICES = "product-item__price"
    COUNT_OF_FOUND_ITEMS = "/ html / body / div[1] / main / div[3] / div / div[1] / div / div[2] / span"

    # get elements
    def getExpandSortOptionsButton(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=self.EXPAND_SORT_OPTIONS_BUTTON)

    def getSortByAscendingPriceButton(self):
        return self.driver.find_element(by=By.XPATH, value=self.SORT_BY_PRICE_ASC_BUTTON)

    def getSortByDescendingPriceButton(self):
        return self.driver.find_element(by=By.XPATH, value=self.SORT_BY_PRICE_DESC_BUTTON)

    # def getPricesOfItems(self):
    #     return self.driver.find_elements(by=By.CLASS_NAME, value=self.ITEMS_PRICES)

    def getCountOfFoundItems(self):
        return int(self.driver.find_element(by=By.XPATH, value=self.COUNT_OF_FOUND_ITEMS).text)

    # actions on elements
    def expandSortingOptions(self):
        self.page_scroll_up()
        sleep(0.2)
        self.getExpandSortOptionsButton().click()

    def sortByAscendingPriceClick(self):
        self.getSortByAscendingPriceButton().click()

    def sortByDescendingPriceClick(self):
        self.getSortByDescendingPriceButton().click()

    def showMoreWhileAvailable(self):
        # last div increases by 1 everytime the "show more" button is pressed, so we have to increase
        self.page_scroll()
        i = 2
        sleep(0.5)
        while True:
            try:
                SHOW_MORE_BUTTON = self.driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/main/div[4]/div[1]/div[{i}]/div/button")
                SHOW_MORE_BUTTON.click()
                i += 1
                sleep(0.5)
                self.page_scroll()
                sleep(0.5)
            except NoSuchElementException:
                break

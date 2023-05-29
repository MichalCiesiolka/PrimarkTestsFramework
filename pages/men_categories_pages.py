from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from TestFramework.base.base_driver import BaseDriver
from TestFramework.pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.action_chains import ActionChains


class MenCategoryPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    CLOTHING_EXPAND = "/html/body/div[1]/main/div[4]/div/div[1]/div/ul/li[2]/button"
    HOODIES_CATEGORY = "/html/body/div[1]/main/div[4]/div/div[1]/div/ul/li[2]/ul/li[6]/a"
    EXPAND_SORT_OPTIONS_BUTTON = "pagination__item--sort-option"
    SORT_BY_PRICE_ASC_BUTTON = "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div[2]/form/div/div/label[5]"
    SORT_BY_PRICE_DESC_BUTTON = "/html/body/div[1]/main/div[3]/div/div[2]/div[1]/div[1]/div[2]/form/div/div/label[6]"

    def getClothingExpand(self):
        return self.driver.find_element(by=By.XPATH, value=self.CLOTHING_EXPAND)

    def getHoodiesCategory(self):
        return self.driver.find_element(by=By.XPATH, value=self.HOODIES_CATEGORY)

    def getExpandSortOptionsButton(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=self.EXPAND_SORT_OPTIONS_BUTTON)

    def getSortByAscendingPriceButton(self):
        return self.driver.find_element(by=By.XPATH, value=self.SORT_BY_PRICE_ASC_BUTTON)

    def getSortByDescendingPriceButton(self):
        return self.driver.find_element(by=By.XPATH, value=self.SORT_BY_PRICE_DESC_BUTTON)

    def expandClothingSubCategory(self):
        self.getClothingExpand().click()
        sleep(0.5)

    def clickHoodiesCategory(self):
        self.getHoodiesCategory().click()
        sleep(0.5)

    def expandSortingOptions(self):
        self.page_scroll_up()
        sleep(0.2)
        self.getExpandSortOptionsButton().click()

    def sortByAscendingPriceClick(self):
        self.getSortByAscendingPriceButton().click()

    def sortByDescendingPriceClick(self):
        self.getSortByDescendingPriceButton().click()

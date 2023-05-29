from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from TestFramework.base.base_driver import BaseDriver
from TestFramework.pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.action_chains import ActionChains


class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    ACCEPT_COOKIES_BUTTON = "onetrust-accept-btn-handler"
    SEARCH_FIELD = "site-search"
    MEN_HOVER_MENU = "/html/body/div[1]/header/div[3]/div/nav/ul/li[2]/a"
    MEN_HOODIES_CATEGORY = "/html/body/div[1]/header/div[3]/div/nav/ul/li[2]/div/div/div[1]/ul/li[2]/a"

    # get elements
    def getAcceptCookiesButton(self):
        return self.driver.find_element(by=By.ID, value=self.ACCEPT_COOKIES_BUTTON)

    def getSearchField(self):
        return self.driver.find_element(by=By.ID, value=self.SEARCH_FIELD)

    def getMenHoverMenu(self):
        return self.driver.find_element(by=By.XPATH, value=self.MEN_HOVER_MENU)

    # actions on elements
    def clickAcceptCookiesButton(self):
        self.getAcceptCookiesButton().click()

    def searchForQuery(self, query):
        self.getSearchField()
        self.getSearchField().clear()
        self.getSearchField().send_keys(query)
        self.getSearchField().send_keys(Keys.RETURN)
        # search_results = SearchResultsPage(self.driver)
        # return search_results

    def clickMenCategory(self):
        self.getMenHoverMenu().click()
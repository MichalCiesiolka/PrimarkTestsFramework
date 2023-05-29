from time import sleep

from TestFramework.pages.men_categories_pages import MenCategoryPage
from TestFramework.pages.primark_launch_page import LaunchPage
from TestFramework.pages.search_results_page import SearchResultsPage
from TestFramework.pages.universal_pages import UniversalPages
from TestFramework.testcases.primtest import *
from TestFramework.utilities.utils import Utils
import softest


@pytest.mark.usefixtures("setup")
class TestSearchForClothing():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
        self.universal = UniversalPages(self.driver)
        self.search_results = SearchResultsPage(self.driver)
        self.SEARCH_QUERY = ["t-shirt", "koszula", "bluza"]

    # test if the prices are sorted correctly when selecting ascending sort
    def test_asc_price_sort(self):
        # accept cookies
        self.lp.clickAcceptCookiesButton()
        # search for query
        self.lp.searchForQuery(self.SEARCH_QUERY[1])
        # sort price by ascending
        self.search_results.expandSortingOptions()
        self.search_results.sortByAscendingPriceClick()
        # scroll to the bottom and click "show more" button while it's present
        self.search_results.showMoreWhileAvailable()
        # get all prices and format them to floats
        PRICES = self.universal.getPrices()
        PRICES = self.ut.format_list_of_prices_to_float(PRICES)
        # assert that the prices are sorted
        self.ut.assert_prices_ascending(PRICES)

    # test if the prices are sorted correctly when selecting descending sort
    def test_desc_price_sort(self):
        self.search_results.expandSortingOptions()
        self.search_results.sortByDescendingPriceClick()
        self.search_results.showMoreWhileAvailable()
        PRICES = self.universal.getPrices()
        PRICES = self.ut.format_list_of_prices_to_float(PRICES)
        self.ut.assert_prices_descending(PRICES)

    # test if the count of items on the page matches the one written on the top of the page
    def test_count_of_items(self):
        items_count = self.search_results.getCountOfFoundItems()
        PRICES = self.universal.getPrices()
        self.ut.assert_correct_amount_of_items(items_count, PRICES)


@pytest.mark.usefixtures("setup")
class TestMenCategoryFilters():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
        self.search_results = SearchResultsPage(self.driver)
        self.universal = UniversalPages(self.driver)
        self.men_category = MenCategoryPage(self.driver)

    # test if hoodies prices are between HIGH and LOW after filtering
    def test_hoodies_price_filter(self):
        LOW = 40
        HIGH = 90
        self.lp.clickAcceptCookiesButton()
        self.lp.clickMenCategory()
        self.men_category.expandClothingSubCategory()
        self.men_category.clickHoodiesCategory()
        self.universal.expandPriceFilter()
        self.universal.narrowPrices(LOW, HIGH)
        prices = self.universal.getPrices()
        prices = self.ut.format_list_of_prices_to_float(prices)
        self.ut.assert_prices_between(prices, LOW, HIGH)


@pytest.mark.usefixtures("setup")
class TestMenCategorySorting():
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()
        self.search_results = SearchResultsPage(self.driver)
        self.universal = UniversalPages(self.driver)
        self.men_category = MenCategoryPage(self.driver)

    def test_hoodies_sort_descending(self):
        self.lp.clickAcceptCookiesButton()
        self.lp.clickMenCategory()
        self.men_category.expandClothingSubCategory()
        self.men_category.clickHoodiesCategory()
        self.men_category.expandSortingOptions()
        self.men_category.sortByDescendingPriceClick()
        PRICES = self.universal.getPrices()
        PRICES = self.ut.format_list_of_prices_to_float(PRICES)
        self.ut.assert_prices_descending(PRICES)

    def test_hoodies_sort_ascending(self):
        self.men_category.expandSortingOptions()
        self.men_category.sortByAscendingPriceClick()
        PRICES = self.universal.getPrices()
        PRICES = self.ut.format_list_of_prices_to_float(PRICES)
        self.ut.assert_prices_ascending(PRICES)

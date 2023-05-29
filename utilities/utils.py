import softest


class Utils(softest.TestCase):
    # def __init__(self):
    #     super().__init__()
    #     self.driver = None

    def format_list_of_prices_to_float(self, prices):
        prices = [price.text for price in prices]
        prices = [price.replace(' PLN', '') for price in prices]
        prices = [price.replace(',', '.') for price in prices]
        prices = [float(price) for price in prices]
        return prices

    def assert_prices_ascending(self, prices):
        self.soft_assert(self.assertTrue, all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1)))

    def assert_prices_descending(self, prices):
        self.soft_assert(self.assertTrue, all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)))

    def assert_correct_amount_of_items(self, count_of_items, list_of_items):
        self.soft_assert(self.assertEqual, len(list_of_items), count_of_items)

    def assert_prices_between(self, prices, low, high):
        self.soft_assert(self.assertTrue, all(low <= prices[i] <= high for i in range(len(prices) - 1)))


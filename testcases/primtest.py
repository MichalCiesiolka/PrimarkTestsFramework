import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    # don't close after test (you have to comment out the yield to make it work)
    options = Options()
    options.add_experimental_option("detach", True)
    # launch chrome and open the website
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.primark.com/pl/")
    driver.maximize_window()
    # pass driver to every class that uses this fixture
    request.cls.driver = driver
    yield
    driver.close()

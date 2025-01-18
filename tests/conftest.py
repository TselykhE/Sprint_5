import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    yield driver
    driver.quit()

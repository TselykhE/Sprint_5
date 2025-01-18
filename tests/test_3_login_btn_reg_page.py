from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators

class TestStellarBurgers:
    def test_login(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))
        browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert constants.LOGIN_PAGE == browser.current_url

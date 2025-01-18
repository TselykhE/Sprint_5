from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators


class TestStellarBurgers:
    def test_transition_through_constructor(self, browser):
        browser.get(constants.LOGIN_PAGE)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUTTON))
        browser.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.CREATE_BURGER))

    def test_transition_through_logo(self, browser):
        browser.get(constants.LOGIN_PAGE)
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGO_STELLAR_BURGERS))
        browser.find_element(*Locators.LOGO_STELLAR_BURGERS).click()
        assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.CREATE_BURGER))

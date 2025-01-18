from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators

class TestStellarBurgers:
    def test_button_bread(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.SAUCE_BUTTON))
        browser.find_element(*Locators.SAUCE_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.BULKI_BUTTON))
        browser.find_element(*Locators.BULKI_BUTTON).click()
        assert 'tab_tab_type_current' in browser.find_element(*Locators.BULKI_BUTTON).get_attribute('class')

    def test_button_sauces(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.FILLING_BUTTON))
        browser.find_element(*Locators.FILLING_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.SAUCE_BUTTON))
        browser.find_element(*Locators.SAUCE_BUTTON).click()
        assert 'tab_tab_type_current' in browser.find_element(*Locators.SAUCE_BUTTON).get_attribute('class')

    def test_button_filling(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.FILLING_BUTTON))
        browser.find_element(*Locators.FILLING_BUTTON).click()
        assert 'tab_tab_type_current' in browser.find_element(*Locators.FILLING_BUTTON).get_attribute('class')

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators

class TestStellarBurgers:
        def test_logout_button(self, browser):
            browser.get(constants.LOGIN_PAGE)
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable(Locators.LOGIN_EMAIL_INPUT))
            browser.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
            browser.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
            browser.find_element(*Locators.LOGIN_BUTTON).click()
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT))
            browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
            WebDriverWait(browser, 5).until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON))
            browser.find_element(*Locators.LOGOUT_BUTTON).click()
            WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON))
            assert constants.LOGIN_PAGE == browser.current_url

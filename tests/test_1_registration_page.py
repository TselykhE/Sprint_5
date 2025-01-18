from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators


class TestStellarBurgers:

    def test_registration_new_user(self, browser):
        browser.get(constants.MAIN_URL)
        email = constants.EMAIL_FOR_LOGIN
        password = constants.PASSWORD_FOR_LOGIN
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        browser.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE))
        browser.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        browser.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(constants.NAME_FOR_REGISTRATION)
        browser.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        browser.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        browser.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        browser.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 7).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
        browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(browser, 15).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_registration_invalid_password(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        browser.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE))
        browser.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        browser.find_element(*Locators.REGISTRATION_NAME_INPUT).send_keys(constants.NAME_FOR_REGISTRATION)
        browser.find_element(*Locators.REGISTRATION_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        browser.find_element(*Locators.REGISTRATION_PASSWORD_INPUT).send_keys('12345')
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(Locators.REGISTRATION_BUTTON))
        browser.find_element(*Locators.REGISTRATION_BUTTON).click()
        assert WebDriverWait(browser, 15).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE))

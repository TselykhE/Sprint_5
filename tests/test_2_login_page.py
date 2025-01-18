from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constants
from locators import Locators


class TestStellarBurgers:
    def test_login_personal_account_button(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable(Locators.LOGIN_IN_ACCOUNT))
        browser.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        browser.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 7).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
        browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(browser, 17).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_login_in_account_button(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        browser.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.LOGIN_EMAIL_INPUT))
        browser.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 11).until(EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT))
        browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(browser, 15).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_login_button_on_registration_page(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        browser.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE))
        browser.find_element(*Locators.REGISTRATION_BUTTON_ON_LOGIN_PAGE).click()
        WebDriverWait(browser, 7).until(EC.presence_of_element_located(Locators.LOGIN_BUTTON_ON_PAGES))
        browser.find_element(*Locators.LOGIN_BUTTON_ON_PAGES).click()
        WebDriverWait(browser, 7).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        browser.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 7).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(browser, 15).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

    def test_login_restore_password_page(self, browser):
        browser.get(constants.MAIN_URL)
        WebDriverWait(browser, 3).until(EC.visibility_of_element_located(Locators.LOGIN_IN_ACCOUNT))
        browser.find_element(*Locators.LOGIN_IN_ACCOUNT).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.RESTORE_PASSWORD_BUTTON))
        browser.find_element(*Locators.RESTORE_PASSWORD_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_ON_PAGES))
        browser.find_element(*Locators.LOGIN_BUTTON_ON_PAGES).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_EMAIL_INPUT))
        browser.find_element(*Locators.LOGIN_EMAIL_INPUT).send_keys(constants.EMAIL_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_PASSWORD_INPUT).send_keys(constants.PASSWORD_FOR_LOGIN)
        browser.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located(Locators.PERSONAL_ACCOUNT))
        browser.find_element(*Locators.PERSONAL_ACCOUNT).click()
        assert WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))

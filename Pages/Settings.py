from hashlib import new
from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor
# from selenium.webdriver.common.action_chains import ActionChains


class Settings:
    def __init__(self, driver):
        self.driver = driver
        # self.actions = ActionChains(driver=driver)

    def enter_click_settings(self):
        htvv= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_settings)))
        htvv.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_settings).click()
        # htvv.click()
        # actions = new.actions(self.driver)
        # actions.moveToElement(htvv).click().build().perform()
        print("وارد قسمت تنظینات شدید.")

    def enter_settings_add(self):
        self.driver.find_element('xpath', settings_add).click()

    def enter_settings_name(self, name):
        self.driver.find_element('xpath', settings_name).send_keys(name)

    def enter_settings_trans(self, trans):
        self.driver.find_element('xpath', settings_trans).send_keys(trans)

    def enter_settings_add_config_form(self, number):
        self.driver.find_element('xpath', settings_add_config_form).send_keys(number)

    def enter_settings_value(self):
        self.driver.find_element('xpath', settings_value).click()

    def enter_settings_value_option(self):
        self.driver.find_element('xpath', settings_value_option).click()

    def enter_settings_save(self):
        self.driver.find_element('xpath', settings_save).click()

    def enter_settings_no_save(self):
        self.driver.find_element('xpath', settings_no_save).click()

    def enter_settings_version(self):
        self.driver.find_element('xpath', settings_version).click()

    def enter_settings_version_option(self):
        self.driver.find_element('xpath', settings_version_option).click()

    def enter_settings_transactions_daily(self):
        self.driver.find_element('xpath', settings_transactions_daily).click()

    def enter_settings_transactions_daily_option(self):
        self.driver.find_element('xpath', settings_transactions_daily_option).click()

    def enter_settings_transactions_monthly(self):
        self.driver.find_element('xpath', settings_transactions_monthly).click()

    def enter_settings_transactions_monthly_option(self):
        self.driver.find_element('xpath', settings_transactions_monthly_option).click()

    def enter_settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS(self):
        self.driver.find_element('xpath', settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS).click()

    def enter_settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS_option(self):
        self.driver.find_element('xpath', settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS_option).click()

    def enter_settings_POD_API_MAX_COUNT(self):
        self.driver.find_element('xpath', settings_POD_API_MAX_COUNT).click()

    def enter_settings_POD_API_MAX_COUNT_option(self):
        self.driver.find_element('xpath', settings_POD_API_MAX_COUNT_option).click()

    def enter_settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT(self):
        self.driver.find_element('xpath', settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT).click()

    def enter_settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT_option(self):
        self.driver.find_element('xpath', settings_FINNOTECH_API_MAX_MONTHLY_TRANSACTION_COUNT_option).click()

    def enter_settings_CAPTCHA(self):
        self.driver.find_element('xpath', settings_CAPTCHA).click()

    def enter_settings_CAPTCHA_option(self):
        self.driver.find_element('xpath', settings_CAPTCHA_option).click()

    def enter_settings_SMS_PANEL(self):
        self.driver.find_element('xpath', settings_SMS_PANEL).click()

    def enter_settings_SMS_PANEL_option(self):
        self.driver.find_element('xpath', settings_SMS_PANEL_option).click()

    def enter_settings_OTP_EXPIRE(self):
        self.driver.find_element('xpath', settings_OTP_EXPIRE).click()

    def enter_settings_OTP_EXPIRE_option(self):
        self.driver.find_element('xpath', settings_OTP_EXPIRE_option).click()

    def enter_settings_TEST_MODE(self):
        self.driver.find_element('xpath', settings_TEST_MODE).click()

    def enter_settings_MAX_OTP_CHECK(self):
        self.driver.find_element('xpath', settings_MAX_OTP_CHECK).click()

    def enter_settings_MAX_OTP_CHECK_option(self):
        self.driver.find_element('xpath', settings_MAX_OTP_CHECK_option).click()

    def enter_settings_TIME_SCOPE_EXPIRE(self):
        self.driver.find_element('xpath', settings_TIME_SCOPE_EXPIRE).click()

    def enter_settings_TIME_SCOPE_EXPIRE_option(self):
        self.driver.find_element('xpath', settings_TIME_SCOPE_EXPIRE_option).click()

    def enter_settings_LOGIN_TIME_EXPIRE(self):
        self.driver.find_element('xpath', settings_LOGIN_TIME_EXPIRE).click()

    def enter_settings_LOGIN_TIME_EXPIRE_option(self):
        self.driver.find_element('xpath', settings_LOGIN_TIME_EXPIRE_option).click()

    def enter_settings_MAX_RETRY_SCOPE(self):
        self.driver.find_element('xpath', settings_MAX_RETRY_SCOPE).click()

    def enter_settings_MAX_RETRY_SCOPE_option(self):
        self.driver.find_element('xpath', settings_MAX_RETRY_SCOPE_option).click()

    def enter_settings_GOOGLE_CAPTCHA_PAGES(self):
        self.driver.find_element('xpath', settings_GOOGLE_CAPTCHA_PAGES).click()

    def enter_settings_REQUIREMENT_BANK_ACCOUNT_REGISTRATION(self):
        self.driver.find_element('xpath', settings_REQUIREMENT_BANK_ACCOUNT_REGISTRATION).click()

    def enter_settings_INCREASE_COEFFICIENT(self):
        self.driver.find_element('xpath', settings_INCREASE_COEFFICIENT).click()

    def enter_settings_INCREASE_COEFFICIENT_option(self):
        self.driver.find_element('xpath', settings_INCREASE_COEFFICIENT_option).click()

    def enter_settings_GOOGLE_2F_AUTH(self):
        self.driver.find_element('xpath', settings_GOOGLE_2F_AUTH).click()

    def enter_settings_WRAPPER_SEND_MESSAGE_BY_SMS(self):
        self.driver.find_element('xpath', settings_WRAPPER_SEND_MESSAGE_BY_SMS).click()

    def enter_settings_WRAPPER_SEND_MESSAGE_BY_SMS_option(self):
        self.driver.find_element('xpath', settings_WRAPPER_SEND_MESSAGE_BY_SMS_option).click()

    def enter_settings_WRAPPER_SEND_PATTERN_BY_SMS(self):
        self.driver.find_element('xpath', settings_WRAPPER_SEND_PATTERN_BY_SMS).click()

    def enter_settings_WRAPPER_SEND_PATTERN_BY_SMS_option(self):
        self.driver.find_element('xpath', settings_WRAPPER_SEND_PATTERN_BY_SMS_option).click()

    def enter_settings_SHAHKAR_PANEL(self):
        self.driver.find_element('xpath', settings_SHAHKAR_PANEL).click()

    def enter_settings_SHAHKAR_PANEL_option(self):
        self.driver.find_element('xpath', settings_SHAHKAR_PANEL_option).click()

    def enter_settings_WRAPPER_SHAHKAR(self):
        self.driver.find_element('xpath', settings_WRAPPER_SHAHKAR).click()

    def enter_settings_WRAPPER_SHAHKAR_option(self):
        self.driver.find_element('xpath', settings_WRAPPER_SHAHKAR_option).click()

    def enter_settings_IPG_JIBIMO_CHECK_NATIONAL_CODE(self):
        self.driver.find_element('xpath', settings_IPG_JIBIMO_CHECK_NATIONAL_CODE).click()

    def enter_settings_CARD_SERVICE_MENU(self):
        self.driver.find_element('xpath', settings_CARD_SERVICE_MENU).click()

    def enter_settings_CARD_SERVICE_MENU_option(self):
        self.driver.find_element('xpath', settings_CARD_SERVICE_MENU_option).click()

    def enter_settings_RAYAN_REQUEST_TIMEOUT(self):
        self.driver.find_element('xpath', settings_RAYAN_REQUEST_TIMEOUT).click()

    def enter_settings_RAYAN_REQUEST_TIMEOUT_option(self):
        self.driver.find_element('xpath', settings_RAYAN_REQUEST_TIMEOUT_option).click()

    def enter_settings_DOMAIN_SEND_SMS(self):
        self.driver.find_element('xpath', settings_DOMAIN_SEND_SMS).click()

    def enter_settings_DOMAIN_SEND_SMS_option(self):
        self.driver.find_element('xpath', settings_DOMAIN_SEND_SMS_option).click()

    def enter_settings_MIN_NAV(self):
        self.driver.find_element('xpath', settings_MIN_NAV).click()

    def enter_settings_MIN_NAV_option(self):
        self.driver.find_element('xpath', settings_MIN_NAV_option).click()

    def enter_settings_MAX_NAV(self):
        self.driver.find_element('xpath', settings_MAX_NAV).click()

    def enter_settings_MAX_NAV_option(self):
        self.driver.find_element('xpath', settings_MAX_NAV_option).click()

    def enter_settings_SEJAM_DEFAULT(self):
        self.driver.find_element('xpath', settings_SEJAM_DEFAULT).click()

    def enter_settings_SEJAM_DEFAULT_option(self):
        self.driver.find_element('xpath', settings_SEJAM_DEFAULT_option).click()

    def enter_settings_WRAPPER_SEJAM(self):
        self.driver.find_element('xpath', settings_WRAPPER_SEJAM).click()

    def enter_settings_WRAPPER_SEJAM_option(self):
        self.driver.find_element('xpath', settings_WRAPPER_SEJAM_option).click()

    def enter_settings_WRAPPER_FUND_REGISTER(self):
        self.driver.find_element('xpath', settings_WRAPPER_FUND_REGISTER).click()

    def enter_settings_WRAPPER_FUND_REGISTER_option(self):
        self.driver.find_element('xpath', settings_WRAPPER_FUND_REGISTER_option).click()

    def enter_settings_IPG_SEP(self):
        self.driver.find_element('xpath', settings_IPG_SEP).click()

    def enter_settings_IPG_PEP(self):
        self.driver.find_element('xpath', settings_IPG_PEP).click()

    def enter_settings_EXPIRE_FUND_LICENSE_AFTER_DAY(self):
        self.driver.find_element('xpath', settings_EXPIRE_FUND_LICENSE_AFTER_DAY).click()

    def enter_settings_EXPIRE_FUND_LICENSE_AFTER_DAY_option(self):
        self.driver.find_element('xpath', settings_EXPIRE_FUND_LICENSE_AFTER_DAY_option).click()

    def enter_settings_PROFIT_CALCULATION_DAY(self):
        self.driver.find_element('xpath', settings_PROFIT_CALCULATION_DAY).click()

    def enter_settings_PROFIT_CALCULATION_DAY_option(self):
        self.driver.find_element('xpath', settings_PROFIT_CALCULATION_DAY_option).click()

    def enter_settings_IPG_SEPEHR(self):
        self.driver.find_element('xpath', settings_IPG_SEPEHR).click()

    def enter_settings_PAYMENT_LINK_GATEWAY(self):
        self.driver.find_element('xpath', settings_PAYMENT_LINK_GATEWAY).click()

    def enter_settings_PAYMENT_LINK_GATEWAY_option(self):
        self.driver.find_element('xpath', settings_PAYMENT_LINK_GATEWAY_option).click()

    def enter_settings_IPG_JIBIMO(self):
        self.driver.find_element('xpath', settings_IPG_JIBIMO).click()

    def enter_settings_BASE_NAV(self):
        self.driver.find_element('xpath', settings_BASE_NAV).click()

    def enter_settings_BASE_NAV_option(self):
        self.driver.find_element('xpath', settings_BASE_NAV_option).click()

    def enter_settings_IPG_SADAD(self):
        self.driver.find_element('xpath', settings_IPG_SADAD).click()

    def enter_(self):
        self.driver.find_element('xpath', settings_FARABOOM_PAYMAN_API_MAX_CONTRACT_EXPIRATION_YEARS).click()

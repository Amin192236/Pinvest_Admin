from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor


class Cashout:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_cashout(self):
        viewcashout= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_cashout)))
        viewcashout.location_once_scrolled_into_view
        # sleep(1)
        self.driver.find_element('xpath', click_cashout).click()

    def enter_cashout_assert(self):
        cashout_assert_text= self.driver.find_element('xpath', cashout_assert).text
        assert cashout_assert_text== "ثبت برداشت کاربران"
        print("با موفقیت وارد قسمت ثبت برداشت کاربران شد.")

    def enter_cashout_user_id(self, code):
        self.driver.find_element('xpath', cashout_user_id).send_keys(code)

    def enter_cashout_fund(self):
        self.driver.find_element('xpath', cashout_fund).click()

    def enter_cashout_unit(self, unit):
        self.driver.find_element('xpath', cashout_unit).send_keys(unit)

    def enter_cashout_date(self):
        self.driver.find_element('xpath', cashout_date).click()

    def enter_cashout_date_next(self):
        self.driver.find_element('xpath', cashout_date_next).click()

    def enter_cashout_date_option(self):
        self.driver.find_element('xpath', cashout_date_option).click()

    def enter_cashout_value(self):
        self.driver.find_element('xpath', cashout_value).click()

    def enter_cashout_submit_btn(self):
        self.driver.find_element('xpath', cashout_submit_btn).click()


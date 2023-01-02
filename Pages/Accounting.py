
from Locators import *


class Accounting:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_accounting(self):
        self.driver.find_element('xpath', click_accounting).click()

    def enter_accounting_assert(self):
        print("با موفقیت وارد قسمت حسابداری شد.")

    def enter_accounting_referral(self, name):
        self.driver.find_element('xpath', accounting_referral).send_keys(name)

    def enter_accounting_referral_btn(self):
        self.driver.find_element('xpath', accounting_referral_btn).click()

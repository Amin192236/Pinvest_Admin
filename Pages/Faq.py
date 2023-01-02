from Locators import *


class Faq:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_faq(self):
        self.driver.find_element('xpath', click_faq).click()

    def enter_faq_assert(self):
        print("شما با موفقیت واردسوالات متداول شدید.")

    def enter_faq_pinvest(self):
        self.driver.find_element('xpath', faq_pinvest).click()

    def enter_faq_account(self):
        self.driver.find_element('xpath', faq_account).click()

    def enter_faq_deposit(self):
        self.driver.find_element('xpath', faq_deposit).click()

    def enter_faq_investment(self):
        self.driver.find_element('xpath', faq_investment).click()

    def enter_faq_funds(self):
        self.driver.find_element('xpath', faq_funds).click()

    def enter_faq_messages(self):
        self.driver.find_element('xpath', faq_messages).click()

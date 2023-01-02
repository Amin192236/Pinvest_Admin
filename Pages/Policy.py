from Locators import *


class PolicyPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_policy(self):
        self.driver.find_element('xpath', click_policy).click()

    def enter_policy_assert(self):
        print("شما با موفقیت وارد قوانین و مقررات شدید.")

    def enter_policy_show(self):
        assert_check_policy= self.driver.find_element('xpath', policy_show).text
        print(assert_check_policy)

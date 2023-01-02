from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor


class Deposit:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_deposit(self):
        html= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_deposit)))
        html.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_deposit).click()

    def enter_deposit_assert(self):
        deposit_assert_text= self.driver.find_element('xpath', deposit_assert).text
        assert deposit_assert_text== "ثبت واریز کاربران"
        print("با موفقیت وارد قسمت ثبت واریز کاربران شد.")

    def enter_deposit_method(self):
        self.driver.find_element('xpath', deposit_method).click()

# # # deposit_pose

    def enter_deposit_pose(self):
        self.driver.find_element('xpath', deposit_pose).click()

    def enter_deposit_pose_bank(self):
        self.driver.find_element('xpath', deposit_pose_bank).click()

    def enter_deposit_pose_bank_option(self):
        self.driver.find_element('xpath', deposit_pose_bank_option).click()

    def enter_deposit_pose_fund(self):
        self.driver.find_element('xpath', deposit_pose_fund).click()

    def enter_deposit_pose_fund_option(self):
        self.driver.find_element('xpath', deposit_pose_fund_option).click()

    def enter_deposit_pose_submit_btn(self):
        self.driver.find_element('xpath', deposit_pose_submit_btn).click()

# # # deposit_receipt

    def enter_deposit_receipt(self):
        self.driver.find_element('xpath', deposit_receipt).click()

    def enter_deposit_receipt_code(self, code):
        self.driver.find_element('xpath', deposit_receipt_code).send_keys(code)

    def enter_deposit_receipt_fund(self):
        self.driver.find_element('xpath', deposit_receipt_fund).click()

    def enter_deposit_receipt_fund_option(self):
        self.driver.find_element('xpath', deposit_receipt_fund_option).click()

    def enter_deposit_receipt_amount(self, amount):
        self.driver.find_element('xpath', deposit_receipt_amount).send_keys(amount)

    def enter_deposit_receipt_date(self):
        self.driver.find_element('xpath', deposit_receipt_date).click()

    def enter_deposit_receipt_date_back(self):
        htmls= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', deposit_receipt_date_back)))
        htmls.location_once_scrolled_into_view
        self.driver.find_element('xpath', deposit_receipt_date_back).click()

    def enter_deposit_receipt_date_option(self):
        self.driver.find_element('xpath', deposit_receipt_date_option).click()

    def enter_deposit_receipt_bank(self):
        # vw= self.driver.find_element('xpath', deposit_receipt_bank)
        # vw.location_once_scrolled_into_view
        self.driver.find_element('xpath', deposit_receipt_bank).click()

    def enter_deposit_receipt_bank_option(self):
        self.driver.find_element('xpath', deposit_receipt_bank_option).click()

    def enter_deposit_receipt_number(self, number):
        self.driver.find_element('xpath', deposit_receipt_number).send_keys(number)

    def enter_deposit_receipt_description(self, description):
        self.driver.find_element('xpath', deposit_receipt_description).send_keys(description)

    def enter_deposit_receipt_submit_btn(self):
        self.driver.find_element('xpath', deposit_receipt_submit_btn).click()


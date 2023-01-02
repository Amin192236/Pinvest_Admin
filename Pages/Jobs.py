from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor


class Jobs:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_jobs(self):
        viewjobs= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('xpath', click_jobs)))
        viewjobs.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_jobs).click()

    def enter_jobs_assert(self):
        print("با موفقیت وارد قسمت جاب ها شد.")

    def enter_jobs_fund(self):
        self.driver.find_element('xpath', jobs_fund).click()

    def enter_jobs_fund_option(self):
        self.driver.find_element('xpath', jobs_fund_option).click()

    def enter_jobs_config_rayanBuy(self):
        self.driver.find_element('xpath', jobs_config_rayanBuy).click()
        print("جاب صدور اجرا شد.")

    def enter_jobs_config_WithdrawJob(self):
        self.driver.find_element('xpath', jobs_config_WithdrawJob).click()
        print("جاب برداشت اجرا شد.")

    def enter_jobs_config_updatesOrdersStatus(self):
        self.driver.find_element('xpath', jobs_config_updatesOrdersStatus).click()
        print("جاب آپدیت وضعیت سفارشات اجرا شد.")

    def enter_jobs_national(self, national):
        self.driver.find_element('xpath', jobs_national).send_keys(national)

    def enter_jobs_config_withdrawWithNationalCode(self):
        self.driver.find_element('xpath', jobs_config_withdrawWithNationalCode).click()
        print("برداشت از طریق کد ملی اجرا شد.")


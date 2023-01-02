
from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor


class Reinvesting:
    def __init__(self, driver):
        self.driver = driver

    def enter_reinvesting_click(self):
        html= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_reinvesting)))
        html.location_once_scrolled_into_view
        self.driver.find_element('xpath', click_reinvesting).click()
        print("با موفقیت وارد قسمت درصد سرمایه گذاری مجدد کاربران شد.")

    def enter_reinvesting_search(self, code):
        self.driver.find_element('xpath', reinvesting_search).send_keys(code)

    def enter_reinvesting_funds(self):
        self.driver.find_element('xpath', reinvesting_funds).click()

    def enter_reinvesting_investment(self):
        self.driver.find_element('xpath', reinvesting_investment).click()

    def enter_reinvesting_investment_option(self):
        self.driver.find_element('xpath', reinvesting_investment_option).click()

    def enter_reinvesting_hide(self):
        self.driver.find_element('xpath', reinvesting_hide).click()

    def enter_reinvesting_funds_name(self):
        funds_name= self.driver.find_element('xpath', reinvesting_funds_name).text
        print("نام صندوق:", funds_name, "می باشد.")

    def enter_reinvesting_result(self):
        table_id = self.driver.find_element('xpath', reinvesting_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)



from Locators import *


class Compass:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_compass(self):
        self.driver.find_element('xpath', click_compass).click()

    def enter_compass_assert(self):
        print("با موفقیت وارد قسمت قطب‌نما شد.")

    def enter_compass_fund(self):
        self.driver.find_element('xpath', compass_fund).click()

    def enter_compass_fund_option(self):
        self.driver.find_element('xpath', compass_fund_option).click()

    def enter_compass_from_date(self):
        self.driver.find_element('xpath', compass_from_date).click()

    def enter_compass_from_date_option(self):
        self.driver.find_element('xpath', compass_from_date_option).click()

    def enter_compass_to_date(self):
        self.driver.find_element('xpath', compass_to_date).click()

    def enter_compass_to_date_option(self):
        self.driver.find_element('xpath', compass_to_date_option).click()

    def enter_compass_chart(self):
        table_id = self.driver.find_element('xpath', compass_chart)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)
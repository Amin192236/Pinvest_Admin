from Locators import *


class Consultations:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_consultations(self):
        self.driver.find_element('xpath', click_consultations).click()

    def enter_consultations_assert(self):
        print("با موفقیت وارد قسمت درخواست های مشاوره شد.")

    def enter_consultations_from_date(self):
        self.driver.find_element('xpath', consultations_from_date).click()

    def enter_consultations_from_date_back(self):
        self.driver.find_element('xpath', consultations_from_date_back).click()

    def enter_consultations_from_date_option(self):
        self.driver.find_element('xpath', consultations_from_date_option).click()

    def enter_consultations_to_date(self):
        self.driver.find_element('xpath', consultations_to_date).click()

    def enter_consultations_to_date_next(self):
        self.driver.find_element('xpath', consultations_to_date_next).click()

    def enter_consultations_to_date_option(self):
        self.driver.find_element('xpath', consultations_to_date_option).click()

    def enter_consultations_switching(self):
        self.driver.find_element('xpath', consultations_switching).click()

    def enter_consultations_result(self):
        table_id = self.driver.find_element('xpath', consultations_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)
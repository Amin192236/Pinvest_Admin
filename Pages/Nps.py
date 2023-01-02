from Locators import *


class Nps:
    def __init__(self, driver):
        self.driver = driver

###nps

    def enter_click_nps(self):
        self.driver.find_element('xpath', click_nps).click()

    def enter_nps_assert(self):
        print("با موفقیت وارد قسمت nps شد.")

    def enter_nps_from_date(self):
        self.driver.find_element('xpath', nps_from_date).click()

    def enter_nps_from_date_option(self):
        self.driver.find_element('xpath', nps_from_date_option).click()

    def enter_nps_to_date(self):
        self.driver.find_element('xpath', nps_to_date).click()

    def enter_nps_to_date_option(self):
        self.driver.find_element('xpath', nps_to_date_option).click()

    def enter_nps_from_score(self):
        self.driver.find_element('xpath', nps_from_score).click()

    def enter_nps_from_score_option(self):
        self.driver.find_element('xpath', nps_from_score_option).click()

    def enter_nps_to_score(self):
        self.driver.find_element('xpath', nps_to_score).click()

    def enter_nps_to_score_option(self):
        self.driver.find_element('xpath', nps_to_score_option).click()

    def enter_nps_search(self, name):
        self.driver.find_element('xpath', nps_search).send_keys(name)

    def enter_nps_result(self):
        table_id = self.driver.find_element('xpath', nps_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_nps_description(self):
        self.driver.find_element('xpath', nps_description).click()

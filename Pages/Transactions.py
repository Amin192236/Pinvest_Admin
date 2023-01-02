from Locators import *


class Transactions:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_transactions(self):
        self.driver.find_element('xpath', click_transactions).click()

    def enter_transactions_from_date(self):
        self.driver.find_element('xpath', transactions_from_date).click()

    def enter_transactions_from_date_back(self):
        self.driver.find_element('xpath', transactions_from_date_back).click()

    def enter_transactions_from_date_option(self):
        self.driver.find_element('xpath', transactions_from_date_option).click()

    def enter_transactions_to_date(self):
        self.driver.find_element('xpath', transactions_to_date).click()

    def enter_transactions_to_date_next(self):
        self.driver.find_element('xpath', transactions_to_date_next).click()

    def enter_transactions_to_date_option(self):
        self.driver.find_element('xpath', transactions_to_date_option).click()

    def enter_transactions_status(self):
        self.driver.find_element('xpath', transactions_status).click()

    def enter_transactions_status_option(self):
        self.driver.find_element('xpath', transactions_status_option).click()

    def enter_transactions_fund(self):
        self.driver.find_element('xpath', transactions_fund).click()

    def enter_transactions_fund_option(self):
        self.driver.find_element('xpath', transactions_fund_option).click()

    def enter_transactions_method(self):
        self.driver.find_element('xpath', transactions_method).click()

    def enter_transactions_method_option(self):
        self.driver.find_element('xpath', transactions_method_option).click()

    def enter_transactions_trace_id_search(self, number):
        self.driver.find_element('xpath', transactions_trace_id_search).send_keys(number)

    def enter_transactions_select_all(self):
        self.driver.find_element('xpath', transactions_select_all).click()

    def enter_transactions_result(self):
        table_id = self.driver.find_element('xpath', transactions_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_transactions_select_option(self):
        self.driver.find_element('xpath', transactions_select_option).click()

    def enter_transactions_approve(self):
        self.driver.find_element('xpath', transactions_approve).click()

    def enter_transactions_reject(self):
        self.driver.find_element('xpath', transactions_reject).click()

# # # transactions_reject_reason

    def enter_transactions_reject_reason(self):
        self.driver.find_element('xpath', transactions_reject_reason).click()

    def enter_transactions_reject_reason_option(self):
        self.driver.find_element('xpath', transactions_reject_reason_option).click()

    def enter_transactions_reject_reason_yes(self):
        self.driver.find_element('xpath', transactions_reject_reason_yes).click()

    def enter_transactions_reject_reason_no(self):
        self.driver.find_element('xpath', transactions_reject_reason_no).click()


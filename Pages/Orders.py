from Locators import *


class Orders:
    def __init__(self, driver):
        self.driver = driver

# # #orders_search

    def enter_orders_click(self):
        self.driver.find_element('xpath', click_orders).click()
        print("با موفقیت وارد قسمت لیست سفارش ها شد.")

    def enter_orders_code_search(self, code):
        self.driver.find_element('xpath', orders_code_search).send_keys(code)

    def enter_orders_name_search(self, name):
        self.driver.find_element('xpath', orders_name_search).send_keys(name)

    def enter_orders_from_date(self):
        self.driver.find_element('xpath', orders_from_date).click()

    def enter_orders_from_date_back(self):
        self.driver.find_element('xpath', orders_from_date_back).click()

    def enter_orders_from_date_option(self):
        self.driver.find_element('xpath', orders_from_date_option).click()

    def enter_orders_to_date(self):
        self.driver.find_element('xpath', orders_to_date).click()

    def enter_orders_to_date_next(self):
        self.driver.find_element('xpath', orders_to_date_next).click()

    def enter_orders_to_date_option(self):
        self.driver.find_element('xpath', orders_to_date_option).click()

    def enter_orders_direct(self):
        self.driver.find_element('xpath', orders_direct).click()

    def enter_orders_indirect(self):
        self.driver.find_element('xpath', orders_indirect).click()

    def enter_orders_fund(self):
        self.driver.find_element('xpath', orders_fund).click()

    def enter_orders_fund_option(self):
        self.driver.find_element('xpath', orders_fund_option).click()

    def enter_orders_status(self):
        self.driver.find_element('xpath', orders_status).click()

    def enter_orders_status_option(self):
        self.driver.find_element('xpath', orders_status_option).click()

    def enter_orders_type(self):
        self.driver.find_element('xpath', orders_type).click()

    def enter_orders_type_option(self):
        self.driver.find_element('xpath', orders_type_option).click()

    def enter_orders_method(self):
        self.driver.find_element('xpath', orders_method).click()

    def enter_orders_method_option(self):
        self.driver.find_element('xpath', orders_method_option).click()

    def enter_orders_referral(self, name):
        self.driver.find_element('xpath', orders_referral).send_keys(name)

    def enter_orders_result(self):
        table_id = self.driver.find_element('xpath', orders_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)


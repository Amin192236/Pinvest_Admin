from Locators import *
from selenium.webdriver.common.keys import Keys


class CustomersPage:
    def __init__(self, driver):
        self.driver = driver

# # #customers_search

    def enter_customers_click(self):
        self.driver.find_element('xpath', click_customers).click()

    def enter_customers_assert(self):
        assert_check_customers= self.driver.find_element('xpath', customers_show).text
        assert assert_check_customers== "همه ی صندوق ها"
        print("با موفقیت وارد قسمت مشتریان شد.")

    def enter_customers_fund(self):
        self.driver.find_element('xpath', customers_fund).click()

    def enter_customers_fund_option(self):
        self.driver.find_element('xpath', customers_fund_option).click()

    def enter_customers_from_date(self):
        self.driver.find_element('xpath', customers_from_date).click()

    def enter_customers_from_date_before(self):
        self.driver.find_element('xpath', customers_from_date_before).click()

    def enter_customers_from_date_option(self):
        self.driver.find_element('xpath', customers_from_date_option).click()

    def enter_customers_to_date(self):
        self.driver.find_element('xpath', customers_to_date).click()

    def enter_customers_to_date_next(self):
        self.driver.find_element('xpath', customers_to_date_next).click()

    def enter_customers_to_date_option(self):
        self.driver.find_element('xpath', customers_to_date_option).click()

    def enter_customers_phone_search(self, code):
        self.driver.find_element('xpath', customers_phone_search).send_keys(code)

    def enter_customers_phone_search_result(self):
        table_id = self.driver.find_element('xpath', customers_phone_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    # def enter_customers_phone_search_result(self):
    #     table_id = self.driver.find_element('xpath', customers_phone_search_result)
    #     for row in table_id:
    #         print(row.text)

# # # customers_name_search

    def enter_customers_name_search(self, name):
        self.driver.find_element('xpath', customers_name_search).send_keys(name)

    def enter_customers_name_search_result(self):
        table_id = self.driver.find_element('xpath', customers_phone_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_customers_search_direct(self):
        self.driver.find_element('xpath', customers_search_direct).click()

    def enter_customers_search_indirect(self):
        self.driver.find_element('xpath', customers_search_indirect).click()

# # #customers

    def enter_customers_referral(self, name):
        self.driver.find_element('xpath', customers_referral).send_keys(name)

    def enter_customers_referral_option(self):
        self.driver.find_element('xpath', customers_referral_option).click()

    def enter_customers_result(self):
        table_id = self.driver.find_element('xpath', customers_phone_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

# # #customers_show_account

    def enter_customers_show_account(self):
        self.driver.find_element('xpath', customers_show_account).click()

    def enter_customers_show_account_name(self):
        name= self.driver.find_element('xpath', customers_show_account_name).text
        print("شما وارد گزارش حساب های", name, "شدید")

# # #customers_show_funds

    def enter_customers_show_funds(self):
        self.driver.find_element('xpath', customers_show_funds).click()

    def enter_customers_show_funds_name(self):
        name= self.driver.find_element('xpath', customers_show_funds_name).text
        print("شما وارد گزارش صندوق های", name, "شدید")


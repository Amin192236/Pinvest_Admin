from Locators import *


class Payment:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_payment(self):
        self.driver.find_element('xpath', click_payment).click()

    def enter_payment_assert(self):
        print("با موفقیت وارد قسمت لینک پرداخت شد.")

# # # payment_send

    def enter_payment_search(self, code):
        self.driver.find_element('xpath', payment_search).send_keys(code)

    def enter_payment_coefficient_fee(self, code):
        self.driver.find_element('xpath', payment_coefficient_fee).send_keys(code)

    def enter_payment_payment_link_name(self, name):
        self.driver.find_element('xpath', payment_payment_link_name).send_keys(name)

    def enter_payment_send(self):
        self.driver.find_element('xpath', payment_send).click()

# # # payment_graph

    def enter_payment_from_date(self):
        self.driver.find_element('xpath', payment_from_date).click()

    def enter_payment_from_date_back(self):
        self.driver.find_element('xpath', payment_from_date_back).click()

    def enter_payment_from_date_option(self):
        self.driver.find_element('xpath', payment_from_date_option).click()

    def enter_payment_to_date(self):
        self.driver.find_element('xpath', payment_to_date).click()

    def enter_payment_to_date_next(self):
        self.driver.find_element('xpath', payment_to_date_next).click()

    def enter_payment_to_date_option(self):
        self.driver.find_element('xpath', payment_to_date_option).click()

# # # payment_actions

    def enter_payment_table_search(self, code):
        self.driver.find_element('xpath', payment_table_search).send_keys(code)

    def enter_payment_referral(self, name):
        self.driver.find_element('xpath', payment_referral).send_keys(name)

    def enter_payment_send_to_link(self):
        self.driver.find_element('xpath', payment_send_to_link).click()

    def enter_payment_copy(self):
        self.driver.find_element('xpath', payment_copy).click()

    def enter_payment_qr(self):
        self.driver.find_element('xpath', payment_qr).click()

    def enter_payment_resend(self):
        self.driver.find_element('xpath', payment_resend).click()

    def enter_payment_resend_no(self):
        self.driver.find_element('xpath', payment_resend_no).click()

    def enter_payment_resend_yes(self):
        self.driver.find_element('xpath', payment_resend_yes).click()

    def enter_payment_edit(self):
        self.driver.find_element('xpath', payment_edit).click()

    def enter_payment_delete(self):
        self.driver.find_element('xpath', payment_delete).click()

# # # payment_edit

    def enter_payment_update_coefficient_fee(self, code):
        self.driver.find_element('xpath', payment_update_coefficient_fee).send_keys(code)

    def enter_payment_update_payment_link_name(self, name):
        self.driver.find_element('xpath', payment_update_payment_link_name).send_keys(name)

    def enter_payment_update_link_modal(self):
        self.driver.find_element('xpath', payment_update_link_modal).click()

    def enter_payment_update_link_confirm(self):
        self.driver.find_element('xpath', payment_update_link_confirm).click()

# # # payment_delete

    def enter_payment_delete_link_modal(self):
        self.driver.find_element('xpath', payment_delete_link_modal).click()

    def enter_payment_delete_link_confirm(self):
        self.driver.find_element('xpath', payment_delete_link_confirm).click()

    # def enter_payment_result(self):
    #     table_id = self.driver.find_element('xpath', payment_result)
    #     for row in range(1, 11):
    #         rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
    #         for row_data in rows:
    #             col = row_data.find_elements('tag name', "td")
    #             for i in range(len(col)):
    #                 print(col[i].text)

from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor
# def wait_until_element_has_an_attribute(element_selector, element_locator, attribute, attribute_value, timeout=5,
#                                         exact=True):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(element_selector, element_locator)
#             if exact:
#                 assert element.get_attribute(attribute) == attribute_value
#             else:
#                 assert attribute_value in element.get_attribute(attribute)
#             return
#         except:
#             sleep(0.2)
#     raise Exception("Element attribute is not: " + str(attribute))


class Invite:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_has_an_attribute(self, element_selector, element_locator, attribute, attribute_value, timeout=5):
        for i in range(timeout * 5):
            try:
                element = self.driver.find_element(element_selector, element_locator)
                element.click()
                # if exact:
                #     assert element.get_attribute(attribute) == attribute_value
                # else:
                #     assert attribute_value in element.get_attribute(attribute)
                return
            except:
                sleep(0.2)
        raise Exception("Element attribute is not: " + str(attribute))

    def enter_click_invite(self):
        viewinvite= WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('xpath', click_invite)))
        viewinvite.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', click_invite).click()

    def enter_invite_assert(self):
        print("با موفقیت وارد قسمت دعوت از دیگران شد.")

    def enter_invite_msisdn(self, msisdn):
        self.driver.find_element('xpath', invite_msisdn).send_keys(msisdn)

    def enter_invite_send_link(self):
        self.driver.find_element('xpath', invite_send_link).click()

    def enter_invite_send_card(self):
        self.driver.find_element('xpath', invite_send_card).click()

    def enter_invite_show_link(self):
        self.driver.find_element('xpath', invite_show_link).click()

    def enter_invite_show_card(self):
        self.driver.find_element('xpath', invite_show_card).click()

    def enter_invite_result(self):
        table_id = self.driver.find_element('xpath', invite_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)
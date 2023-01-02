from time import sleep

from Locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# import org.openqa.selenium.JavascriptExecutor


class Users:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_users(self):
        html= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', click_users)))
        html.location_once_scrolled_into_view
        self.driver.find_element('xpath', click_users).click()

    def enter_users_assert(self):
        # assert_check_users= self.driver.find_element('xpath', users_add).text
        # assert assert_check_users== "افزودن معرف"
        print("شما با موفیت وارد قسمت معرف شدید. ")

# # # users_Add

    def enter_users_add(self):
        self.driver.find_element('xpath', users_add).click()

    def enter_users_type(self):
        self.driver.find_element('xpath', users_type).click()

    def enter_users_type_option(self):
        self.driver.find_element('xpath', users_type_option).click()

    def enter_users_first_name(self, name):
        self.driver.find_element('xpath', users_first_name).send_keys(name)

    def enter_users_last_name(self, name):
        self.driver.find_element('xpath', users_last_name).send_keys(name)

    def enter_users_national_code(self, code):
        self.driver.find_element('xpath', users_national_code).send_keys(code)

    def enter_users_phone_number(self, number):
        self.driver.find_element('xpath', users_phone_number).send_keys(number)

    def enter_users_username_delete(self):
        username= self.driver.find_element('xpath', users_username).click()
        username.send_keys(Keys.DELETE).perform()

    def enter_users_username(self, username):
        self.driver.find_element('xpath', users_username).send_keys(username)

    def enter_users_password(self, password):
        self.driver.find_element('xpath', users_password).send_keys(password)

    def enter_users_password_confirmation(self, password):
        self.driver.find_element('xpath', users_password_confirmation).send_keys(password)

    def enter_users_role_id(self):
        # role= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', users_role_id)))
        # role.location_once_scrolled_into_view
        self.driver.find_element('xpath', users_role_id).click()
        # self.driver.find_element('xpath', users_role_id).click()

    def enter_users_role_option(self):
        self.driver.find_element('xpath', users_role_option).click()

    def enter_users_parent(self, parent):
        self.driver.find_element('xpath', users_parent).send_keys(parent)

    def enter_users_shaba_number(self, number):
        self.driver.find_element('xpath', users_shaba_number).send_keys(number)

    def enter_users_bank_id(self):
        ba= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', users_bank_id)))
        ba.location_once_scrolled_into_view
        self.driver.find_element('xpath', users_bank_id).click()

    def enter_users_bank_option(self):
        self.driver.find_element('xpath', users_bank_option).click()

    def enter_users_cac(self, cac):
        self.driver.find_element('xpath', users_cac).send_keys(cac)

    def enter_users_address(self, address):
        self.driver.find_element('xpath', users_address).send_keys(address)

    def enter_users_add_donat_save(self):
        self.driver.find_element('xpath', users_save_no).click()

    def enter_users_add_save_role_button(self):
        html= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', users_save_user_button)))
        html.location_once_scrolled_into_view
        self.driver.find_element('xpath', users_save_user_button).click()
        # self.driver.find_element('xpath', users_save_user_button).click()

# # # users_edit
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

    def enter_users_edit(self):
        u_edit= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', users_edit)))
        u_edit.location_once_scrolled_into_view
        self.driver.find_element('xpath', users_edit).click()

    def enter_users_edit_assert(self):
        assert_check_users= self.driver.find_element('xpath', users_edit_assert).text
        assert assert_check_users== "ویرایش معرف"
        print("شما با موفیت وارد قسمت: ", assert_check_users, " شدید." )

    def enter_users_edit_national_code(self):
        assert_check_users= self.driver.find_element('xpath', users_edit_national_code).text
        print("کد ملی معرف: ", assert_check_users, " می باشد." )

    def enter_users_edit_username(self):
        assert_check_users= self.driver.find_element('xpath', users_edit_username).text
        print("نام کاربری معرف: ", assert_check_users, " می باشد." )

    def enter_users_edit_first_name(self, name):
        self.driver.find_element('xpath', users_edit_first_name).send_keys(name)

    def enter_users_edit_last_name(self, name):
        self.driver.find_element('xpath', users_edit_last_name).send_keys(name)

    def enter_users_edit_phone_number(self, number):
        self.driver.find_element('xpath', users_edit_phone_number).send_keys(number)

    def enter_users_edit_parent(self, parent):
        self.driver.find_element('xpath', users_edit_parent).send_keys(parent)

    def enter_users_edit_role(self):
        self.driver.find_element('xpath', users_edit_role).click()

    def enter_users_edit_role_option(self):
        self.driver.find_element('xpath', users_edit_role_option).click()

    def enter_users_edit_shaba(self, shaba):
        self.driver.find_element('xpath', users_edit_shaba).send_keys(shaba)

    def enter_users_edit_bank(self):
        self.driver.find_element('xpath', users_edit_bank).click()

    def enter_users_edit_bank_option(self):
        self.driver.find_element('xpath', users_edit_bank_option).click()

    def enter_users_edit_address(self, address):
        self.driver.find_element('xpath', users_edit_address).send_keys(address)

    def enter_users_edit_save_no(self):
        self.driver.find_element('xpath', users_edit_save_no).click()

    def enter_users_edit_save_user_button(self):
        self.driver.find_element('xpath', users_edit_save_user_button).click()

# # # change_password

    def enter_users_change_password(self):
        u_password= WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(('xpath', users_change_password)))
        u_password.location_once_scrolled_into_view
        self.driver.find_element('xpath', users_change_password).click()

    def enter_users_change_password_assert(self):
        assert_check_users= self.driver.find_element('xpath', users_change_password_assert).text
        print("شما با موفیت وارد قسمت: ", assert_check_users, " شدید." )

    def enter_users_change_password_new(self, password):
        self.driver.find_element('xpath', users_change_password_new).send_keys(password)

    def enter_users_change_password_show(self):
        self.driver.find_element('xpath', users_change_password_show).click()

    def enter_users_change_password_confirmation(self, password):
        self.driver.find_element('xpath', users_change_password_confirmation).send_keys(password)

    def enter_users_change_password_confirmation_show(self):
        self.driver.find_element('xpath', users_change_password_confirmation_show).click()

    def enter_users_change_password_no(self):
        self.driver.find_element('xpath', users_change_password_no).click()

    def enter_users_change_password_yes(self):
        self.driver.find_element('xpath', users_change_password_yes).click()

# # # users_deactivation_activation

    def enter_users_deactivation(self):
        self.driver.find_element('xpath', users_deactivation).click()

    def enter_users_deactivation_assert(self):
        assert_deactivation= self.driver.find_element('xpath', users_deactivation_assert).text
        print(assert_deactivation)

    def enter_users_deactivation_no(self):
        self.driver.find_element('xpath', users_deactivation_no).click()

    def enter_users_deactivation_yes(self):
        self.driver.find_element('xpath', users_deactivation_yes).click()

# # # Users_Search

    def enter_users_search_role(self):
        self.driver.find_element('xpath', users_search_role).click()

    def enter_users_search_role_option(self):
        self.driver.find_element('xpath', users_search_role_option).click()

    def enter_users_search_from_date(self):
        self.driver.find_element('xpath', users_search_from_date).click()

    def enter_users_search_from_date_back(self):
        self.driver.find_element('xpath', users_search_from_date_back).click()

    def enter_users_search_from_date_option(self):
        self.driver.find_element('xpath', users_search_from_date_option).click()

    def enter_users_search_to_date(self):
        self.driver.find_element('xpath', users_search_to_date).click()

    def enter_users_search_to_date_next(self):
        self.driver.find_element('xpath', users_search_to_date_next).click()

    def enter_users_search_to_date_option(self):
        self.driver.find_element('xpath', users_search_to_date_option).click()

    def enter_users_search_code(self, code):
        self.driver.find_element('xpath', users_search_code).send_keys(code)

    def enter_users_search_result(self):
        table_id = self.driver.find_element('xpath', users_search_result)
        for row in range(1, 11):
            rows = table_id.find_elements('xpath', "//body//tbody//tr[" + str(row) + "]")
            for row_data in rows:
                col = row_data.find_elements('tag name', "td")
                for i in range(len(col)):
                    print(col[i].text)

    def enter_users_search_direct(self):
        self.driver.find_element('xpath', users_search_direct).click()

    def enter_users_search_indirect(self):
        self.driver.find_element('xpath', users_search_indirect).click()

    def enter_users_search_name(self, name):
        self.driver.find_element('xpath', users_search_name).send_keys(name)

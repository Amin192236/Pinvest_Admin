from Locators import *


class Roles:
    def __init__(self, driver):
        self.driver = driver

    def enter_click_roles(self):
        self.driver.find_element('xpath', click_roles).click()

    def enter_roles_assert(self):
        assert_check_roles= self.driver.find_element('xpath', roles_add).text
        assert assert_check_roles== "افزودن نقش"
        print("شما با موفیت وارد قسمت: ",assert_check_roles, " شدید." )

# # # Roles_Add

    def enter_roles_add(self):
        self.driver.find_element('xpath', roles_add).click()

    def enter_roles_add_name(self, name):
        self.driver.find_element('xpath', roles_add_name).send_keys(name)

    def enter_roles_add_permission_all(self):
        self.driver.find_element('xpath', roles_add_permission_all).click()

    def enter_roles_add_permission1(self):
        self.driver.find_element('xpath', roles_add_permission1).click()

    def enter_roles_add_permission2(self):
        self.driver.find_element('xpath', roles_add_permission2).click()

    def enter_roles_add_permission3(self):
        self.driver.find_element('xpath', roles_add_permission3).click()

    def enter_roles_add_access_role_id(self):
        self.driver.find_element('xpath', roles_add_access_role_id).click()

    def enter_roles_add_donat_save(self):
        self.driver.find_element('xpath', roles_add_donat_save).click()

    def enter_roles_add_save_role_button(self):
        self.driver.find_element('xpath', roles_add_save_role_button).click()

# # # Roles_edit

    def enter_roles_edit(self):
        self.driver.find_element('xpath', roles_edit).click()

    def enter_roles_edit_button(self):
        self.driver.find_element('xpath', roles_edit_button).click()

# # # Roles_delete

    def enter_roles_delete(self):
        self.driver.find_element('xpath', roles_delete).click()

    def enter_roles_delete_no(self):
        self.driver.find_element('xpath', roles_delete_no).click()

    def enter_roles_delete_button(self):
        self.driver.find_element('xpath', roles_delete_button).click()



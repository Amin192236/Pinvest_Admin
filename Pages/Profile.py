from Locators import *


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

# Profile

    def enter_click_profile(self):
        self.driver.find_element('xpath', click_profile).click()

    def enter_profile_full_name(self):
        full_name= self.driver.find_element('xpath', profile_full_name).get_attribute('value')
        print("نام شما:", full_name, "می باشد")

    def enter_profile_national_code(self):
        national_code = self.driver.find_element('xpath', profile_national_code).get_attribute('value')
        print("کد ملی شما:", national_code, "می باشد")

    def enter_profile_sejam(self):
        sejam= self.driver.find_element('xpath', profile_sejam).get_attribute('value')
        print("کد سجام شما:", sejam, "می باشد")

    def enter_profile_sejam_edit(self):
        self.driver.find_element('xpath', profile_sejam_edit).click()

    def enter_profile_bank(self):
        bank= self.driver.find_element('xpath', profile_bank).get_attribute('value')
        print("نام بانک شما:", bank, "می باشد")

    def enter_profile_birthday(self):
        birthday= self.driver.find_element('xpath', profile_birthday).get_attribute('value')
        print("تاریخ تولد شما: ", birthday, "می باشد")

    def enter_profile_phone_number(self):
        phone_number= self.driver.find_element('xpath', profile_phone_number).get_attribute('value')
        print("شماره موبایل شما: ", phone_number, "می باشد")

    def enter_profile_phone_number_edit(self):
        self.driver.find_element('xpath', profile_phone_number_edit).click()

    def enter_profile_phone_number_new(self, number):
        self.driver.find_element('xpath', profile_phone_number_new).send_keys(number)

    def enter_profile_phone_number_btn(self):
        self.driver.find_element('xpath', profile_phone_number_btn).click()

    def enter_profile_education(self):
        self.driver.find_element('xpath', profile_education).click()

    def enter_profile_education_option(self):
        self.driver.find_element('xpath', profile_education_option).click()

# change_password

    def enter_profile_change_password(self):
        self.driver.find_element('xpath', profile_change_password).click()

    def enter_profile_change_password_previous(self, previous):
        self.driver.find_element('xpath', profile_change_password_previous).send_keys(previous)

    def enter_profile_change_password_previous_show(self):
        self.driver.find_element('xpath', profile_change_password_previous_show).click()

    def enter_profile_change_password_new(self, newpass):
        self.driver.find_element('xpath', profile_change_password_new).send_keys(newpass)

    def enter_profile_change_password_new_show(self):
        self.driver.find_element('xpath', profile_change_password_new_show).click()

    def enter_profile_change_password_confirmation(self, confirmation):
        self.driver.find_element('xpath', profile_change_password_confirmation).send_keys(confirmation)

    def enter_profile_change_password_confirmation_show(self):
        self.driver.find_element('xpath', profile_change_password_confirmation_show).click()

    def enter_profile_change_password_opt_out(self):
        self.driver.find_element('xpath', profile_change_password_opt_out).click()

    def enter_profile_change_password_btn(self):
        self.driver.find_element('xpath', profile_change_password_btn).click()

    def enter_profile_btn(self):
        self.driver.find_element('xpath', profile_btn).click()

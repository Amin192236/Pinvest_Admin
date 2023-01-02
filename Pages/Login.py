from Locators import *


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, name):
        self.driver.find_element('xpath', username).send_keys(name)

    def enter_password(self, code):
        self.driver.find_element('xpath', password).send_keys(code)

    def enter_show_password(self):
        self.driver.find_element('xpath', show_password).click()

    def enter_btn_submit(self):
        self.driver.find_element('xpath', btn_submit).click()

    def enter_site_header(self):
        assert_check_login= self.driver.find_element('xpath', site_header).text
        # assert assert_check_login== "پینوست"
        assert assert_check_login== "کل کارمزد ساخته شده من"
        # print("شما با موفقیت وارد ", assert_check_login, "شدید.")
        print("شما با موفقیت وارد پنل ادمین پینوست شدید ")

    def enter_logout(self):
        self.driver.find_element('xpath', logout).click()

    def enter_logout_no(self):
        self.driver.find_element('xpath', logout_no).click()

    def enter_logout_yes(self):
        self.driver.find_element('xpath', logout_yes).click()


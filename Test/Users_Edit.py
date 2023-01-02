from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Pages.Find_Element import FindElement
from Pages.Users import Users
from Pages.Login import LoginPage
from Locators import *
import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="E:\PRG_Test\Pinvest_Admin\chromedriver.exe")


class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        # cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)


    def test01_login_register(self):
        self.driver.get("https://admin-ha1.pinvest.ir/signin")
        login = LoginPage(driver=self.driver)
        login.enter_username("superadmin")
        login.enter_password("1234kaKA!")
        login.enter_show_password()
        login.enter_btn_submit()
        sleep(2)
        login.enter_site_header()
        # login.enter_logout()
        # login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()

    # def test02_users(self):
    #     users = Users(driver=self.driver)
    #     users.enter_click_users()
    #     users.enter_users_assert()

# # # users_edit

    def test03_users_edit(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        # self.driver.refresh()
        users.enter_click_users()
        # users.enter_users_assert()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        findel.wait_until_element_has_an_attribute('xpath', users_edit, 'class', 'icon pi-edit')
        # users.enter_users_edit()
        # users.enter_users_edit_save_user_button()
        # users.enter_users_edit()
        users.enter_users_edit_assert()
        users.enter_users_edit_national_code()
        users.enter_users_edit_username()
        users.enter_users_edit_first_name("Test")
        users.enter_users_edit_last_name("Test")
        users.enter_users_edit_phone_number("001")
        users.enter_users_edit_parent("Test")
        findel.wait_until_element_has_an_attribute('xpath', users_edit_role, 'name', 'role')
        # users.enter_users_edit_role()
        users.enter_users_edit_role_option()
        users.enter_users_edit_shaba("000000")
        findel.wait_until_element_has_an_attribute('xpath', users_edit_bank, 'name', 'bank')
        # users.enter_users_edit_bank()
        users.enter_users_edit_bank_option()
        users.enter_users_edit_address("Test")
        # sleep(2)
        findel.wait_until_element_has_an_attribute('xpath', users_edit_save_no, 'class', 'btn border-primary bg-transparent')
        # users.enter_users_edit_save_no()

# # # change_password

    def test04_users_change_password(self):
        users = Users(driver=self.driver)
        findel = FindElement(driver=self.driver)
        users.enter_click_users()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        findel.wait_until_element_has_an_attribute('xpath', users_change_password, 'class', '  w-0')
        # users.enter_users_change_password()
        users.enter_users_change_password_assert()
        findel.wait_until_element_has_an_attribute('xpath', users_change_password_yes, 'class', 'btn btn-primary')
        # users.enter_users_change_password_yes()
        users.enter_users_change_password_new("12345678")
        users.enter_users_change_password_show()
        users.enter_users_change_password_confirmation("1234567899")
        users.enter_users_change_password_confirmation_show()
        users.enter_users_change_password_no()
        # self.driver.refresh()
        print(" تمام المان های بخش تغییر رمز معرف بررسی شدند. ")

# # # users_deactivation_activation

    def test05_users_deactivation_activation(self):
        users = Users(driver=self.driver)
        # findel = FindElement(driver=self.driver)
        # findel.wait_until_element_has_an_attribute('xpath', click_users, 'href', '/users')
        self.driver.refresh()
        users.enter_click_users()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        users.enter_users_deactivation()
        # users.enter_users_deactivation_no()
        # users.enter_users_deactivation()
        # users.enter_users_deactivation_assert()
        # users.enter_users_deactivation_yes()
        driver.refresh()
        print("شما با موفقیت یک یوزر را غیرفعال و فعال کردید.")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()

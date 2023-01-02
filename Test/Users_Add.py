from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Users import Users
from Pages.Login import LoginPage

import unittest

# o = Options()
# o.add_argument('--no-sandbox')
#
# s = Service('d:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path="E:\PRG_Test\Pinvest_Admin\chromedriver.exe")


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

# # # users_Add

    def test02_users_add(self):
        users = Users(driver=self.driver)
        users.enter_click_users()
        users.enter_users_assert()
        users.enter_users_add()
        users.enter_users_type()
        users.enter_users_type_option()
        users.enter_users_first_name("Test_Name")
        users.enter_users_last_name("Test")
        users.enter_users_national_code("12345678")
        users.enter_users_phone_number("09309303333")
        # # # users.enter_users_username_delete()
        users.enter_users_username("UsernameTest")
        users.enter_users_password("Test12345678*")
        users.enter_users_password_confirmation("Test12345678*")
        # users.enter_users_role_id()
        # users.enter_users_role_option()
        users.enter_users_parent("کیانوش آریانفر")
        users.enter_users_shaba_number("123456789987654321123456")
        sleep(2)
        # users.enter_users_bank_id()
        # users.enter_users_bank_option()
        users.enter_users_cac("100")
        users.enter_users_address("تهران میرداماد خیابان نفت شمالی")
        # users.enter_users_add_donat_save()
        # users.enter_users_add_save_role_button()
        print("متاسفانه نمیتونم معرف اضافه کنم چون کدهای ولید میخواد و من ندارم :) ")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()

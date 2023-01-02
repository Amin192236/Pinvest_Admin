from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options
from Pages.Login import LoginPage
from Pages.Users import Users


import unittest

o = Options()
o.add_argument('--no-sandbox')

s = Service('d:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Pinvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=s, options=o)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    def test01_login_register(self):
        self.driver.get("https://admin-ha1.pinvest.ir/signin")
        login = LoginPage(driver=self.driver)
        login.enter_username("superadmin")
        login.enter_password("1234kaKA!")
        login.enter_show_password()
        login.enter_btn_submit()
        sleep(3)
        login.enter_site_header()
        # login.enter_logout()
        # login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()

    def test02_users(self):
        users = Users(driver=self.driver)
        users.enter_click_users()
        users.enter_users_assert()

# # # users_phone_search

    def test03_users_phone_search(self):
        users = Users(driver=self.driver)
        users.enter_users_search_role()
        users.enter_users_search_role_option()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        users.enter_users_search_to_date()
        users.enter_users_search_to_date_next()
        users.enter_users_search_to_date_option()
        users.enter_users_search_code("4120")
        sleep(1)
        users.enter_users_search_result()

    def test04_users_phone_search_direct(self):
        users = Users(driver=self.driver)
        users.enter_users_search_direct()
        sleep(1)
        users.enter_users_search_result()

    def test05_users_phone_search_indirect(self):
        users = Users(driver=self.driver)
        users.enter_users_search_indirect()
        sleep(1)
        users.enter_users_search_result()

# # # users_name_search

    def test06_users_name_search(self):
        users = Users(driver=self.driver)
        self.driver.refresh()
        users.enter_users_search_role()
        users.enter_users_search_role_option()
        users.enter_users_search_from_date()
        users.enter_users_search_from_date_back()
        users.enter_users_search_from_date_option()
        users.enter_users_search_to_date()
        users.enter_users_search_to_date_next()
        users.enter_users_search_to_date_option()
        users.enter_users_search_name("کیانوش")
        sleep(1)
        users.enter_users_search_result()

    def test07_users_name_search_direct(self):
        users = Users(driver=self.driver)
        users.enter_users_search_direct()
        sleep(1)
        users.enter_users_search_result()

    def test08_users_name_search_indirect(self):
        users = Users(driver=self.driver)
        users.enter_users_search_indirect()
        sleep(1)
        users.enter_users_search_result()






    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_reports, click_reports_users_invited
from Pages.Find_Element import FindElement
from Pages.Login import LoginPage
from Pages.Reports import Reports


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
        sleep(3)
        login.enter_site_header()
        # login.enter_logout()
        # login.enter_logout_no()
        # login.enter_logout()
        # login.enter_logout_yes()

# # # reports_users_invited_phone_search

    def test02_reports_users_invited_phone_search(self):
        reports= Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # reports.enter_click_reports()
        findel.wait_until_element_has_an_attribute('xpath', click_reports_users_invited, 'href', '/reports/users-invited')
        # reports.enter_click_reports_users_invited()
        # assert reports
        reports.enter_reports_users_invited_assert()
        reports.enter_reports_users_invited_phone_search("4120")
        reports.enter_reports_users_invited_from_date()
        reports.enter_reports_users_invited_from_date_back()
        reports.enter_reports_users_invited_from_date_option()
        reports.enter_reports_users_invited_to_date()
        reports.enter_reports_users_invited_to_date_next()
        reports.enter_reports_users_invited_to_date_option()
        sleep(1)
        reports.enter_reports_users_invited_phone_search_result()

# # # reports_users_invited_phone_search

    def test03_enter_reports_users_invited_name_search(self):
        reports = Reports(driver=self.driver)
        self.driver.refresh()
        reports.enter_reports_users_invited_name_search("کیانوش")
        sleep(1)
        reports.enter_reports_users_invited_phone_search_result()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()

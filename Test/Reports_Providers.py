from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.chrome.options import Options

from Locators import click_reports, click_reports_providers
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

# # # reports_providers

    def test02_reports_providers(self):
        reports = Reports(driver=self.driver)
        findel = FindElement(driver=self.driver)
        findel.wait_until_element_has_an_attribute('xpath', click_reports, 'class', 'cursor_pointer')
        # sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', click_reports_providers, 'href', '/reports/providers')
        # reports.enter_click_reports_providers()
        findel.lod_page()
        # assert reports
        reports.enter_reports_providers_assert()
        reports.enter_reports_providers_value_report_1()
        reports.enter_reports_providers_report_1_month()
        # reports.enter_reports_providers_report_1_month_option()
        reports.enter_reports_providers_report_1_year()
        reports.enter_reports_providers_report_1_year_option()
        reports.enter_reports_providers_report_1_graph()
        reports.enter_reports_providers_report_1_graph()
        reports.enter_reports_providers_report_1_fund()
        sleep(1)
        reports.enter_reports_providers_report_1_fund_result()
        reports.enter_reports_providers_report_1_fund()
        reports.enter_reports_providers_value_report_2()
        reports.enter_reports_providers_report_2_month()
        reports.enter_reports_providers_report_2_month_option()
        reports.enter_reports_providers_report_2_year()
        reports.enter_reports_providers_report_2_year_option()
        reports.enter_reports_providers_report_2_graph()
        reports.enter_reports_providers_report_2_graph()
        reports.enter_reports_providers_report_2_fund()
        sleep(1)
        reports.enter_reports_providers_report_2_fund_result()
        reports.enter_reports_providers_report_2_fund()


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
